from django.db import models
from django.db.models import CASCADE
from rest_framework import serializers

from leagueapi.models import UserProfile
from leagueapi.models.Team import Team


class Player(UserProfile):
    user_type = "PLAYER"
    team = models.ForeignKey( Team, on_delete=CASCADE, related_name='players')
    height = models.FloatField()
    average_score = models.FloatField(default=0)
    number_of_games = models.IntegerField(default=0)


class PlayerBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('user_name', 'team', 'height')
