"""
Django settings

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_DIR = os.path.join(BASE_DIR, 'django')
APPS_DIR = os.path.join(DJANGO_DIR, 'apps')

# add the main django path to the pythonpath
sys.path.insert(0, DJANGO_DIR)

# add the apps path to the pythonpath
sys.path.insert(0, APPS_DIR)

# don't generate .pyc files
sys.dont_write_bytecode = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9643587734045xa+*^mi+@rWFDWFQDFQDW9643587734'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# this is a security feature to prevent host spoofing in production
ALLOWED_HOSTS = ['*']

# installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'debug_toolbar',
    'web',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(DJANGO_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

# locations of uploaded media
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
MEDIA_URL = '/media/'

# additional locations of static files to collect
STATICFILES_DIRS = (
    os.path.join(DJANGO_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'

# http://django-debug-toolbar.readthedocs.org/
INTERNAL_IPS = ('127.0.0.1', '::1', '192.168.33.1')
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True,
}

# use HTTPS/SSL
USE_SSL = False

# local/development settings will override the production settings above
try:
    from settings_local import *
except ImportError as e:
    pass

# use HTTPS/SSL in production
if USE_SSL:
    PROTOCOL = 'https://'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # header passed from NGINX to indicate secure requests
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

# use HTTP for local development
else:
    PROTOCOL = 'http://'
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_PROXY_SSL_HEADER = None
    SECURE_SSL_REDIRECT = False
