FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Установка postgresql-client для проверки доступности базы данных
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "weather_project.wsgi:application", "--bind", "0.0.0.0:8000"]