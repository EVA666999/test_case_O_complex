from rest_framework import serializers
from .models import WeatherData, SearchHistory
from django.db import models

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'city', 'temperature']

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ['city', 'search_count', 'last_search']


