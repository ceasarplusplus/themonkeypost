"""
Django settings for monkeypost project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '6ba5t@&i*pqe7@vllgpbpb&g0-6(-0=#if#ilxf(0wu*vte7ub'
SECRET_KEY = config('SECRET_KEY')
# with open(os.path.join(BASE_DIR, 'monkeypost/secret_key.txt')) as f:
#     SECRET_KEY = f.read().strip()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['157.245.254.139', 'www.themonkeypost.net', 'themonkeypost.net', 'monkeypost.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'home',
    'news',
    'store',
    'order',
    'users',
    'ckeditor',
    'ckeditor_uploader',
    'mptt',
    'crispy_forms',
    'django_countries',
    'taggit',
    # 'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'storages',
]

SITE_ID = 1

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware', #debugtool bar
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'monkeypost.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'monkeypost.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'monkeypostdb',
#         'USER': 'ceasar',
#         'PASSWORD': '@1Monkey_king',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# databade .ini
DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}


# ...
SITE_ID = 1

####################################
##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'images/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}


###################################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

ROBOTS_SITEMAP_URLS = [
    'https://www.themonkeypost.net/sitemap.xml',
    'https://www.themonkeypost.net/news_sitemap.xml'
]


# =============== Dev settings ===========================================

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





# ================== Prod setting ======================================

# email settings .ini --->
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')


# email settings --->

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'mail.privateemail.com'
# EMAIL_HOST_USER = 'info@themonkeypost.net'
# EMAIL_HOST_PASSWORD = 'monkeypost@1Admin'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
# DEFAULT_FROM_EMAIL = 'info@themonkeypost.net'







AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_SIGNATURE_VERSION = 's3v4'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# # STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'

MEDIA_URL =  f'https://{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'

STATICFILES_STORAGE =  'custom_storages.StaticStorage'

DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'



SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CORS_REPLACE_HTTPS_REFERER      = True
# HOST_SCHEME                     = "http://"
# SECURE_PROXY_SSL_HEADER         = None
# SECURE_SSL_REDIRECT             = True
# SESSION_COOKIE_SECURE           = True
# CSRF_COOKIE_SECURE              = True


# this 3
# SECURE_HSTS_SECONDS             = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_PRELOAD = True


# SECURE_FRAME_DENY               = True


# SECURE_BROWSER_XSS_FILTER = True


