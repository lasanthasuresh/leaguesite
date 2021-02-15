from django.db import models
from django.db.models import CASCADE
from rest_framework import serializers

from leagueapi.models.Team import Team
from leagueapi.models.Tournament import Tournament


class Round(models.Model):
    round_name = models.CharField(max_length=60)
    tournament = models.ForeignKey(Tournament, on_delete=CASCADE, related_name='rounds')
    qualified_teams = models.ManyToManyField(Team, related_name='qualified_rounds')

    def __str__(self):
        return f"{self.tournament} {self.round_name}"


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Round
        fields = ('round_name', 'tournament')
