from datetime import datetime

from django.contrib.auth import user_logged_out, user_logged_in
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.dispatch import receiver


class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='sessions')
    started = models.DateTimeField()
    ended = models.DateTimeField(null=True)
    session_duration = models.IntegerField(null=True)
    session_ended = models.BooleanField(default=False)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    user_session = UserSession.objects.create(user=user, started=datetime.now())
    user_session.save()


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):

    # here I do an assumption that only one would exist for a user with session_ended=False which can be wrong.
    # the scenarios that falsify the assumption are considered out of scope for this assignment.

    current_session = UserSession.objects\
        .filter(user=user).filter(session_ended=False)\
        .first()

    current_session.ended = datetime.now()
    current_session.session_duration = (current_session.ended - current_session.started).seconds
    current_session.session_ended = True
    current_session.save()
