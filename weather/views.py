from typing import Optional
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import requests
from .models import SearchHistory, WeatherData
from .serializers import SearchHistorySerializer, WeatherDataSerializer

def index(request):
    return render(request, 'weather/search.html')

class WeatherViewSet(viewsets.ReadOnlyModelViewSet):
    """Weather data retrieval through Open-Meteo API"""
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    @swagger_auto_schema(
        operation_description="Get weather for a specific city",
        manual_parameters=[
            openapi.Parameter(
                'city',
                openapi.IN_QUERY,
                description="City name",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: "Weather data",
            404: "City not found"
        }
    )
    @action(detail=False, methods=['get'])
    def get_weather(self, request):
        """Get weather for a specific city"""
        city = request.query_params.get('city')
        if not city:
            return Response(
                {"error": "City parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        coords = self.get_coordinates(city)
        if not coords:
            return Response(
                {"error": f"City '{city}' not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Save search history
        self.save_search_history(city)

        temperature = self.get_temperature(coords)
        return Response({
            'city': city,
            'temperature': temperature,
            'coordinates': coords
        })

    def get_coordinates(self, city: str) -> Optional[dict]:
        """Get city coordinates from Open-Meteo API"""
        response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city}
        ).json()
        results = response.get("results") # coordinates
        if results:
            return {
                'latitude': results[0]["latitude"],
                'longitude': results[0]["longitude"]
            }
        return None

    def get_temperature(self, coords: dict) -> float:
        """Get current temperature for given coordinates"""
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                **coords,
                "current_weather": True
            }
        ).json()
        return response["current_weather"]["temperature"]

    def save_search_history(self, city: str) -> None:
        """Save city search history"""
        history, created = SearchHistory.objects.get_or_create(city=city)
        if not created:
            history.search_count += 1
            history.save()

class WeatherView(View):
    def get(self, request):
        city = request.GET.get('city')
        weather = {}
        error = None
        if city:
            geo_resp = requests.get(
                "https://geocoding-api.open-meteo.com/v1/search",
                params={"name": city}
            ).json()
            results = geo_resp.get("results")
            if results:
                coords = {
                    'latitude': results[0]["latitude"],
                    'longitude': results[0]["longitude"]
                }
                temp_resp = requests.get(
                    "https://api.open-meteo.com/v1/forecast",
                    params={**coords, "current_weather": True}
                ).json()
                weather = {
                    'city': city,
                    'temperature': temp_resp["current_weather"]["temperature"],
                    'coordinates': coords
                }
                history, created = SearchHistory.objects.get_or_create(city=city)
                history.search_count = (history.search_count or 0) + 1
                history.save()
            else:
                error = f"City '{city}' not found"
        return render(request, 'weather/search.html', {'weather': weather, 'error': error})

class SearchHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """API: список всех городов с количеством поисков"""
    queryset = SearchHistory.objects.all().order_by('-search_count')
    serializer_class = SearchHistorySerializer

