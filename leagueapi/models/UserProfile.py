from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=60,unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(class)s_user_profile")

    class Meta:
        abstract = True

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.username



