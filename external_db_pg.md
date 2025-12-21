```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'app_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 60, # Closed after 60 seconds of inactivity
        'CONN_HEALTH_CHECKS': True, # Django checks if the connection is still alive, Reconnects automatically if it’s broken
    }
}
```
