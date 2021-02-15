from django.db import models
from rest_framework import serializers

from leagueapi.models.Coach import Coach


class Team(models.Model):
    team_name = models.CharField(max_length=60)
    coach = models.OneToOneField(
        Coach,
        on_delete=models.DO_NOTHING
    )
    average_score = models.FloatField(default=0)
    number_of_games = models.IntegerField(default=0)
    number_of_wins = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name


class TeamBaseSerializer(serializers.ModelSerializer):
    coach = serializers.PrimaryKeyRelatedField(many=False,read_only=False,queryset=Coach.objects.all())
    class Meta:
        model = Team
        fields = ('team_name', 'coach')
