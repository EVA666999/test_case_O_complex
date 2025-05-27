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

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
from django.views import View
from .models import WeatherData, SearchHistory
from .serializers import WeatherDataSerializer
from .services import fetch_weather_data, record_search


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
                'city', openapi.IN_QUERY,
                description="City name", type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: "Weather data",
            400: "City required",
            404: "City not found"
        }
    )
    @action(detail=False, methods=['get'])
    def get_weather(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "City parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        weather = fetch_weather_data(city)
        if not weather:
            return Response({"error": f"City '{city}' not found"}, status=status.HTTP_404_NOT_FOUND)

        record_search(city)
        return Response(weather)


class WeatherView(View):
    def get(self, request):
        city = request.GET.get('city')
        context = {"weather": {}, "error": None}

        if city:
            weather = fetch_weather_data(city)
            if weather:
                context["weather"] = weather
                record_search(city)
            else:
                context["error"] = f"City '{city}' not found"

        return render(request, 'weather/search.html', context)

class SearchHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """API: список всех городов с количеством поисков"""
    queryset = SearchHistory.objects.all().order_by('-search_count')
    serializer_class = SearchHistorySerializer

