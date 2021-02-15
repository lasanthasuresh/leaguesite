from rest_framework import serializers

from leagueapi.models import UserProfile


class Coach(UserProfile):
    user_type = "COACH"


class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ('user_name', 'user_type')
