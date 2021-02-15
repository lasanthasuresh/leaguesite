from rest_framework import serializers

from leagueapi.models.UserProfile import UserProfile


class Admin(UserProfile):
    user_type = "ADMIN"


class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ('user_name', 'user_type')
