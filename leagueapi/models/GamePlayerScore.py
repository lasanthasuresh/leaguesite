from django.db import models
from django.db.models import DO_NOTHING, CASCADE
from rest_framework import serializers

from leagueapi.models.Game import Game
from leagueapi.models.Player import Player


class GamePlayerScore(models.Model):
    player = models.ForeignKey(Player, on_delete=DO_NOTHING, related_name='game_statistics')
    game = models.ForeignKey(Game, on_delete=CASCADE, related_name='players')
    score = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return f"{self.player} {self.game} {self.score}"


class GamePlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GamePlayerScore
        fields = ('player', 'game', 'score')
