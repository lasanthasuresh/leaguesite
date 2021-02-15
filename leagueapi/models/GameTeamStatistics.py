from django.db import models
from django.db.models import CASCADE
from rest_framework import serializers

from leagueapi.models.Game import Game
from leagueapi.models.Team import Team


class GameTeamStatistics(models.Model):
    game = models.ForeignKey(Game, on_delete=CASCADE, related_name='teams')
    team = models.ForeignKey(Team, on_delete=CASCADE, related_name='game_statistics')
    is_won_team = models.BooleanField(default=False)
    final_score = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return self.game + " " + self.team


class GameTeamStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameTeamStatistics
        fields = ('game', 'team', 'is_won_team', 'final_score')
