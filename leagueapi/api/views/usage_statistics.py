from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from leagueapi.models import UserSession
from leagueapi.permissions import IsAdmin


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsAdmin))
def get_online_users(request):
    online_users = UserSession.objects.filter(session_ended=False).all()

    online_users = map(lambda s: s.user, online_users)

    serializer = UserSerializer(instance=online_users)

    content = {
        'data': serializer.data
    }

    return Response(content)


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsAdmin))
def get_user_usage(request):
    username = request.GET['username']

    user = User.objects.filter(username=username).findOne()

    user_sessions = UserSession.objects.filter(user=user).all()

    total_amount_of_time = 0
    number_of_logins = 0

    for session in user_sessions:
        total_amount_of_time = session.session_duration
        number_of_logins += 1

    content = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'total_amount_of_time': total_amount_of_time,
        'number_of_logins': number_of_logins
    }

    return Response(content)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name ')
