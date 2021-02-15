from django.db import models
from django.db.models import CASCADE
from rest_framework import serializers

from leagueapi.models.Round import Round


class RoundGroup(models.Model):
    round = models.ForeignKey(Round, on_delete=CASCADE,related_name='groups')
    group_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.round} - {self.group_name}"


class RoundGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoundGroup
        fields = ('round', 'group_name')
