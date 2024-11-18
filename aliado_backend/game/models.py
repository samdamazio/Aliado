from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_games")
    players = models.ManyToManyField(User, related_name="games")
    state = models.JSONField(default=dict)  # Armazena o estado do tabuleiro
    is_active = models.BooleanField(default=True)

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)