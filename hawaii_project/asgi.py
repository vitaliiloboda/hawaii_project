"""
ASGI config for hawaii_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hawaii_project.settings')

django_asgi_app = get_asgi_application()

import meeting.routing
from .token_auth_middleware import JwtAuthMiddleware



application = ProtocolTypeRouter({
    'http': django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            JwtAuthMiddleware(
                AuthMiddlewareStack(URLRouter(meeting.routing.websocket_urlpatterns))
            )
        ),
})
