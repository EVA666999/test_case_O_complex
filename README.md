# Weather Application

Веб-приложение для отображения погоды с использованием Django и OpenWeatherMap API.

## Реализованные функции

- Поиск погоды по названию города
- Автодополнение городов при вводе
- Отображение текущей погоды с детальной информацией
- Сохранение истории поиска
- Статистика поиска (топ городов и последние поиски)
- REST API для работы с погодой и историей поиска
- Swagger документация API
- Удобаный Frontend

## Технологии

- **Backend:**
  - Python 3.10
  - Django 4.2
  - Django REST Framework
  - PostgreSQL
  - psycopg2
  - drf-yasg (Swagger)

- **Frontend:**
  - HTML/CSS
  - JavaScript
  - Bootstrap
  - jQuery

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/EVA666999/test_case_-_komplex.git
cd test_case_-_komplex
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корне проекта:
```env
POSTGRES_DB=weather_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

5. Создайте базу данных PostgreSQL:
```bash
psql -U postgres
CREATE DATABASE weather_db;
```

6. Примените миграции:
```bash
python manage.py migrate
```

7. Запустите сервер разработки:
```bash
python manage.py runserver
```

Приложение будет доступно по адресу: http://localhost:8000

## API Endpoints

- `/api/weather/` - получение погоды по городу
- `/api/search-history/` - история поиска
- `/api/docs/` - Swagger документация API

