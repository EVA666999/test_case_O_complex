from weather.models import SearchHistory
from weather.serializers import SearchHistorySerializer

def test_search_history_serializer():
    history = SearchHistory(city="London", search_count=5)
    serializer = SearchHistorySerializer(history)
    data = dict(serializer.data)
    assert data['city'] == "London"
    assert data['search_count'] == 5
    assert 'last_search' in data
