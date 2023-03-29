from django.contrib.auth.models import User, AnonymousUser
from django.db import models

from users.models import RegUser


class Game(models.Model):
    scores = models.PositiveSmallIntegerField()
    time = models.TimeField()
    user = models.ForeignKey(RegUser, models.CASCADE)
