"""
WSGI config for messagingSystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# web server getway interface - providing standard interface between applications built with django and web servers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messagingSystem.settings')

application = get_wsgi_application()
