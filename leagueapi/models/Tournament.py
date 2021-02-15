from django.db import models
from rest_framework import serializers


class Tournament(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name

    def to_serialized_form(self):
        serializer = TournamentSerializer(self)
        return serializer.data


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('name', 'description', 'date')
