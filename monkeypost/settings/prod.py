from .base import *

DEBUG = False

ALLOWED_HOSTS = ['67.205.150.17', 'www.themonkeypost.net', 'themonkeypost.net', 'monkeypost.herokuapp.com']

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

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# AWS_ACCESS_KEY_ID = 'HHJVZLP6UBSP7CVJLSTA'
# AWS_SECRET_ACCESS_KEY = 'paxmBiMeays6bD2nSszYu7gVmkpZoPZO3wMLkPBZMLs'
# AWS_STORAGE_BUCKET_NAME = 'themonkeypost-space'
# AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = True

# CORS_REPLACE_HTTPS_REFERER      = True
# HOST_SCHEME                     = "http://"
# SECURE_PROXY_SSL_HEADER         = None
# SECURE_SSL_REDIRECT             = True
# SESSION_COOKIE_SECURE           = True
# CSRF_COOKIE_SECURE              = True
SECURE_HSTS_SECONDS             = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_PRELOAD = True
# SECURE_FRAME_DENY               = True


# SECURE_BROWSER_XSS_FILTER = True


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')