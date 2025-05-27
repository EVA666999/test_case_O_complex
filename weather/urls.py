from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherView, WeatherViewSet, SearchHistoryViewSet

router = DefaultRouter()
router.register(r'weather', WeatherViewSet, basename='weather')
router.register(r'search-history', SearchHistoryViewSet, basename='search-history')

urlpatterns = [
    path('', WeatherView.as_view(), name='weather'),
    path('api/', include(router.urls)),
]