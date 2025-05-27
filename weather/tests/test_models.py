import pytest
from weather.models import SearchHistory

@pytest.mark.django_db
def test_search_history_str():
    history = SearchHistory.objects.create(city="Berlin", search_count=2)
    assert str(history) == "Berlin - 2 searches"

@pytest.mark.django_db
def test_search_history_defaults():
    history = SearchHistory.objects.create(city="Paris")
    assert history.search_count == 0
    assert history.city == "Paris"
    assert history.last_search is not None
    assert history.created_at is not None
