from django.conf import settings
from django.db import models


class Game(models.Model):
    scores = models.PositiveSmallIntegerField()
    time = models.TimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
