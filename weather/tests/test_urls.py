import pytest
from django.urls import reverse, resolve
from weather.views import WeatherView, WeatherViewSet, SearchHistoryViewSet

@pytest.mark.django_db
def test_root_url_resolves_to_weather_view():
    resolver = resolve('/')
    assert resolver.func.view_class == WeatherView

def test_search_history_list_url():
    url = reverse('search-history-list')
    assert url == '/api/search-history/'

def test_weather_list_url():
    url = reverse('weather-list')
    assert url == '/api/weather/'

def test_search_history_detail_url():
    # Проверяем, что detail url строится корректно
    url = reverse('search-history-detail', args=[1])
    assert url == '/api/search-history/1/'

def test_weather_detail_url():
    url = reverse('weather-detail', args=[1])
    assert url == '/api/weather/1/'
