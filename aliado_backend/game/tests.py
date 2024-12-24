from django.test import TestCase
from channels.testing import WebsocketCommunicator
from aliado_backend.asgi import application

class WebSocketTestCase(TestCase):
    async def test_websocket_communication(self):
        # Simula uma conexão WebSocket
        communicator = WebsocketCommunicator(application, "/ws/game/test_room/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        # Envia uma mensagem
        message = {"type": "chat.message", "message": "Hello, WebSocket!"}
        await communicator.send_json_to(message)

        # Recebe uma resposta
        response = await communicator.receive_json_from()
        self.assertEqual(response, {"type": "chat.message", "message": "Hello, WebSocket!"})

        # Fecha a conexão
        await communicator.disconnect()