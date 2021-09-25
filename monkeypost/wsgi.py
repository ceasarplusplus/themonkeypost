"""
WSGI config for monkeypost project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import dotenv
import pathlib

from django.core.wsgi import get_wsgi_application

dotenv.load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monkeypost.settings.dev')


if os.getenv('DJANGO_SETTINGS_MODULE'):
 os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')


application = get_wsgi_application()
