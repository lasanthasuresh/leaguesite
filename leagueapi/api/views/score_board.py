from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import serializers

from leagueapi.models import Tournament, Round, GameTeamStatistics, Team, RoundGroup, Game


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_score_board(request):
    # for now, lets only load the latest Tournament
    tournament = Tournament.objects.latest('date')

    if tournament is None:
        raise Http404

    serializer = TournamentSerializer(instance=tournament)
    content = {
        'tournament': serializer.data
    }

    return Response(content)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('pk', 'team_name')


class GameTeamStatisticsSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True, many=False)

    class Meta:
        model = GameTeamStatistics
        fields = ('team', 'final_score')


class GameSerializer(serializers.ModelSerializer):
    teams = GameTeamStatisticsSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('game_name', 'teams')


class GameRoundSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = RoundGroup
        fields = ('group_name', 'games')


class RoundSerializer(serializers.ModelSerializer):
    groups = GameRoundSerializer(many=True, read_only=True)
    qualified_teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Round
        fields = ('round_name', 'groups', 'qualified_teams')


class TournamentSerializer(serializers.ModelSerializer):
    rounds = RoundSerializer(many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = ('name', 'description', 'date', 'rounds')
