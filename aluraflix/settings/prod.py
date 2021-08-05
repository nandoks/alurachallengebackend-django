from .dev import *
import os


SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'https://nandoks-api-alurachallengeback.herokuapp.com/',]

