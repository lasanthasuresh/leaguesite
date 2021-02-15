
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from leagueapi.api.views.player_info import get_player_info
from leagueapi.api.views.score_board import get_score_board
from leagueapi.api.views.team_info import get_all_teams, get_team_info, search_team_plyers
from leagueapi.api.views.usage_statistics import get_online_users, get_user_usage
from leagueapi.api.views.crud.ViewSets import *

router = routers.DefaultRouter()
router.register(r'admin', AdminViewSet)
router.register(r'coach', CoachViewSet)
router.register(r'game', GameViewSet)
router.register(r'game-player-score', GamePlayerScoreViewSet)
router.register(r'game-team-statistics', GameTeamStatisticsViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'round', RoundViewSet)
router.register(r'round-group', RoundGroupViewSet)
router.register(r'team', TeamViewSet)
router.register(r'tournament', TournamentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/crud/', include(router.urls)),
    path('api/player/', get_player_info),
    path('api/scoreboard/', get_score_board),
    path('api/team/all', get_all_teams),
    path('api/team/info', get_team_info),
    path('api/team/players', search_team_plyers),
    path('api/usage/current-users', get_online_users),
    path('api/usage/user-usage', get_user_usage),
]
