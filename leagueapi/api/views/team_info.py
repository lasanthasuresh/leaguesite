from django.http import HttpResponseBadRequest
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import numpy as np

from leagueapi.models import Team, UserProfile, Player, Coach
from leagueapi.permissions import IsAdmin, IsAdminOrCoach, IsCoach


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsAdmin))
def get_all_teams(request):
    teams = Team.objects.all()

    serializer = TeamFullSerializer(teams, many=True)
    content = {
        'data': serializer.data
    }

    return Response(content)


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsAdminOrCoach))
def get_team_info(request):
    team_id = request.GET.get('team-id', None)
    if team_id is None:
        raise HttpResponseBadRequest

    team = Team.objects.get(pk=team_id)

    serializer = TeamFullSerializer(instance=team)

    content = {
        'data': serializer.data
    }

    return Response(content)


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsCoach))
def search_team_plyers(request):
    team_id = request.GET['team-id']
    percentile = request.GET['percentile']

    if team_id is None:
        raise HttpResponseBadRequest

    if percentile is None:
        percentile = 0.9

    team = Team.objects.get(pk=team_id)

    players = team.players

    matching_players = find_players_by_average_score(players, percentile)

    serializer = PlayerSerializer(instance=matching_players)

    content = {
        'data': serializer.data
    }

    return Response(content)


def find_players_by_average_score(players, percentile):
    scores = map(lambda p: p.average_score, players)
    arr = np.array(list(scores))
    percentile = np.percentile(arr, percentile * 100)
    return list(filter(lambda p: p.average_score >= percentile, players))


# region Serializers

class CoachSerializer(serializers.ModelSerializer):
    u_first_name = serializers.CharField(source='user.first_name')
    u_last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Coach
        fields = ('pk', 'username', 'u_first_name', 'u_last_name')


class PlayerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Player
        fields = ('pk', 'username', 'first_name', 'last_name', 'average_score', 'number_of_games')


class TeamFullSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(many=False, read_only=True)
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('team_name', 'coach', 'players', 'average_score', 'number_of_games')

# endregion
