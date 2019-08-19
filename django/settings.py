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
DEBUG = True

# this is a security feature to prevent host spoofing in production
ALLOWED_HOSTS = ['*']

# the main domain for the application
SITE_DOMAIN = 'dvang.party'

# use HTTPS/SSL in production
USE_SSL = True
PROTOCOL = 'https://'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# redirect insecure requests to HTTPS
SECURE_SSL_REDIRECT = True

# don't redirect these paths (e.g. health check)
SECURE_REDIRECT_EXEMPT = [r'^health_check$']

# header passed from NGINX to indicate secure requests
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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


# Cache Table
# https://docs.djangoproject.com/en/2.2/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',  # cache table name
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


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

# local/development settings will override the production settings above
try:
    from settings_local import *
except ImportError as e:
    pass

# use HTTP for local development
if not USE_SSL:
    PROTOCOL = 'http://'
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_PROXY_SSL_HEADER = None
    SECURE_SSL_REDIRECT = False
