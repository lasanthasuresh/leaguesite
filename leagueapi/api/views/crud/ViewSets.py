from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from leagueapi.models.Admin import *
from leagueapi.models.Coach import *
from leagueapi.models.Game import *
from leagueapi.models.GamePlayerScore import *
from leagueapi.models.GameTeamStatistics import *
from leagueapi.models.Player import *
from leagueapi.models.Round import *
from leagueapi.models.RoundGroup import *
from leagueapi.models.Team import *
from leagueapi.models.Tournament import *


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class AdminViewSet(BaseViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class CoachViewSet(BaseViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class GameViewSet(BaseViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GamePlayerScoreViewSet(BaseViewSet):
    queryset = GamePlayerScore.objects.all()
    serializer_class = GamePlayerScoreSerializer


class GameTeamStatisticsViewSet(BaseViewSet):
    queryset = GameTeamStatistics.objects.all()
    serializer_class = GameTeamStatisticsSerializer


class PlayerViewSet(BaseViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerBaseSerializer


class RoundViewSet(BaseViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class RoundGroupViewSet(BaseViewSet):
    queryset = RoundGroup.objects.all()
    serializer_class = RoundGroupSerializer


class TeamViewSet(BaseViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamBaseSerializer


class TournamentViewSet(BaseViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
