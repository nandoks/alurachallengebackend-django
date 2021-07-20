from .base import *
import environ

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

env = environ.Env()
environ.Env.read_env()

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # sqlite3 configuration
        # 'ENGINE': 'django.db.backends.sqlite3'
        # 'NAME': os.path.join(BASE_DIR, 'aluraflix')

        # docker postgres configuration
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'aluraflixdb',
        'PORT': 5432
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

