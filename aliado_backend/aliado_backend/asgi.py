import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from game.routing import websocket_urlpatterns  # Importando as rotas WebSocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliado_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Certifique-se de configurar corretamente essas rotas
        )
    ),
})