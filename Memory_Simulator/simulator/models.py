from django.contrib.auth.models import User, AnonymousUser
from django.db import models


class Game(models.Model):
    scores = models.PositiveSmallIntegerField()
    time = models.TimeField()
    user = models.ForeignKey(User, models.CASCADE)
