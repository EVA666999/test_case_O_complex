# Weather Search API

A web application for weather search with search history tracking and statistics API.

## Features

- Weather search by city name
- City name autocomplete
- Search history tracking
- Search statistics API
- Swagger API documentation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd weather-app
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
pip install -r requirements.txt
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Run the server:
```bash
python manage.py runserver
```

## API Endpoints

### Weather
- `GET /api/weather/search_page/` - Weather search page
- `GET /api/weather/get_weather/?city={city_name}` - Get weather for a specific city

### Search History
- `GET /api/search-history/city_stats/?city={city_name}` - Get statistics for a specific city
- `GET /api/search-history/all_stats/` - Get statistics for all cities
- `GET /api/search-history/top_cities/` - Get top 5 most searched cities
- `GET /api/search-history/recent_searches/` - Get last 5 searches

### Swagger Documentation
- `GET /swagger/` - Swagger UI
- `GET /redoc/` - ReDoc UI

## API Response Examples

### Weather Data
```json
{
    "city": "London",
    "temperature": 15.5,
    "coordinates": {
        "latitude": 51.5074,
        "longitude": -0.1278
    }
}
```

### City Statistics
```json
{
    "city": "London",
    "search_count": 5,
    "last_search": "2024-03-14T12:00:00Z",
    "rank": 2,
    "total_searches": 100
}
```

### Top Cities
```json
[
    {
        "city": "London",
        "search_count": 5,
        "last_search": "2024-03-14T12:00:00Z"
    },
    {
        "city": "Paris",
        "search_count": 3,
        "last_search": "2024-03-14T11:00:00Z"
    }
]
```

## Technologies

- Python 3.8+
- Django 4.2+
- Django REST Framework
- Open-Meteo API
- Bootstrap 5
- Swagger/OpenAPI

## License

MIT 