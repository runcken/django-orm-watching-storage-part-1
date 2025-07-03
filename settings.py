import os
from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
NAME = os.getenv('NAME')
USER_BASE = os.getenv('USER_BASE')
PASSWORD = os.getenv('PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER_BASE,
        'PASSWORD': PASSWORD
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
