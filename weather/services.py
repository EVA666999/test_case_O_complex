import requests
from typing import Optional

from .models import SearchHistory


def fetch_weather_data(city: str) -> Optional[dict]:
    """Получить координаты и температуру для указанного города через Open-Meteo"""
    geo_resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city}
    ).json()

    results = geo_resp.get("results") # тут координаты города
    if not results:
        return None

    coords = {
        'latitude': results[0]["latitude"],
        'longitude': results[0]["longitude"]
    }

    temp_resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={**coords, "current_weather": True}
    ).json()

    return {
        'city': city,
        'coordinates': coords,
        'temperature': temp_resp["current_weather"]["temperature"]
    }


def record_search(city: str) -> None:
    """Сохранить/обновить историю поиска города"""
    history, created = SearchHistory.objects.get_or_create(city=city)
    history.search_count = (history.search_count or 0) + 1
    history.save()
