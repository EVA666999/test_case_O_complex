from django.db import models
from django.utils import timezone

# Create your models here.

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"

class SearchHistory(models.Model):
    city = models.CharField(max_length=100, unique=True)
    search_count = models.PositiveIntegerField(default=0)
    last_search = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-search_count', '-last_search']
        verbose_name_plural = "Search histories"

    def __str__(self):
        return f"{self.city} - {self.search_count} searches"
