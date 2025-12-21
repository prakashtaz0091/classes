# For Django 
```python
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files (optional)
RUN python manage.py collectstatic --noinput

# Run with Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--workers=4", "--bind=0.0.0.0:8000"]
```
# Docker compose for (Django + PostgreSQL + PgBouncer)
```python
version: "3.9"

services:
  postgres:
    image: postgres:15
    container_name: postgres
    restart: always
    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: app_user
      POSTGRES_PASSWORD: app_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  pgbouncer:
    image: edoburu/pgbouncer:1.21.0
    container_name: pgbouncer
    restart: always
    depends_on:
      - postgres
    ports:
      - "6432:6432"
    environment:
      DB_HOST: postgres
      DB_PORT: 5432
      DB_USER: app_user
      DB_PASSWORD: app_password
      DB_NAME: app_db
      POOL_MODE: transaction
      MAX_CLIENT_CONN: 200
      DEFAULT_POOL_SIZE: 20
    volumes:
      - ./pgbouncer/pgbouncer.ini:/etc/pgbouncer/pgbouncer.ini

  django:
    build: .
    container_name: django
    restart: always
    depends_on:
      - pgbouncer
    environment:
      DATABASE_NAME: app_db
      DATABASE_USER: app_user
      DATABASE_PASSWORD: app_password
      DATABASE_HOST: pgbouncer
      DATABASE_PORT: 6432
    ports:
      - "8000:8000"
    command: gunicorn config.wsgi:application --workers=4 --bind=0.0.0.0:8000

volumes:
  postgres_data:
```

# PgBouncer configuration

`pgbouncer/pgbouncer.ini`
```
[databases]
app_db = host=postgres port=5432 dbname=app_db

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432

auth_type = trust

pool_mode = transaction

max_client_conn = 200
default_pool_size = 20

server_idle_timeout = 60
server_lifetime = 300

log_connections = 1
log_disconnections = 1
```

# Django database settings (with PgBouncer)
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),  # pgbouncer
        "PORT": os.getenv("DATABASE_PORT"),  # 6432
        "CONN_MAX_AGE": 0,  # REQUIRED with PgBouncer
    }
}
```


# Startup command
```bash
docker-compose up --build -d
```
# Mental Model
```
Gunicorn workers
        ↓
     PgBouncer
        ↓
    PostgreSQL

```


