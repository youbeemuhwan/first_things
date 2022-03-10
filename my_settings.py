from pathlib import Path #기존에 settings.py 에 있는 코드


SECRET_KEY = 'django-insecure-sg8d5c&23lsfv)qy4%cr498trg12jr(=v4t%bau!-4vj##%3i+'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
    }
}
