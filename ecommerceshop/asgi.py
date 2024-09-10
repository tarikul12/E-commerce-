import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from decouple import config
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("DJANGO_SETTINGS_MODULE"))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerceshop.settings')
ASGI_APPLICATION = "config.asgi.application"
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # We will add WebSocket protocol later. For now, it's just HTTP.
    }
)