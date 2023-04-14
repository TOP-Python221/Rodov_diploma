from django.conf import settings
from django.db import models

from users.models import RegUser


class Game(models.Model):
    scores = models.PositiveSmallIntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, null=True)
