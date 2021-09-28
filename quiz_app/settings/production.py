from .base import *

ALLOWED_HOSTS = ['54.221.44.86']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'walkover_quiz',
        'USER': 'quiz',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'POST': '3306',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}