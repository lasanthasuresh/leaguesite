from django.http import HttpResponseBadRequest
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from leagueapi.models import Player


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_player_info(request):
    player_id = request.GET['player-id']
    if player_id is None:
        raise HttpResponseBadRequest

    team = Player.objects.get(pk=player_id)

    serializer = PlayerFullSerializer(instance=team)

    content = {
        'data': serializer.data
    }

    return Response(content)


class PlayerFullSerializer(serializers.HyperlinkedModelSerializer):
    team_name = serializers.CharField(source='team.team_name')

    class Meta:
        model = Player
        fields = ('user_name', 'team_name', 'height', 'average_score', 'number_of_games')
