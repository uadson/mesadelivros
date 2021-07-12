import environ

from .base import *


env = environ.Env(
    DEBUG = (bool, False)
)

SECRET_KEY = env("SECRET_KEY")

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db()
}

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')