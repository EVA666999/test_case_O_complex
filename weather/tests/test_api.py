import pytest
from typing import cast
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.response import Response
from weather.models import SearchHistory

@pytest.mark.django_db
def test_search_history_api_list():
    # Подготовка данных
    SearchHistory.objects.create(city="London", search_count=5)
    SearchHistory.objects.create(city="Moscow", search_count=3)

    # Запрос к API
    client = APIClient()
    url = reverse('search-history-list')
    response = cast(Response, client.get(url))

    # Проверки
    assert response.status_code == 200

    data = response.json()
    results = data.get('results', data)  # поддержка пагинации и без неё

    assert any(
        item['city'] == 'London' and item['search_count'] == 5
        for item in results
    )
    assert any(
        item['city'] == 'Moscow' and item['search_count'] == 3
        for item in results
    )
