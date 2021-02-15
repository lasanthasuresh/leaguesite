from django.db import models
from django.db.models import CASCADE, DO_NOTHING
from rest_framework import serializers

from leagueapi.models.RoundGroup import RoundGroup
from leagueapi.models.Team import Team


class Game(models.Model):
    game_name = models.CharField(max_length=100)
    group = models.ForeignKey(RoundGroup, on_delete=CASCADE,related_name='games')

    def __str__(self):
        return self.game_name


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('game_name', 'group', 'is_draw')
