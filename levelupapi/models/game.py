
from django.db import models

class Games(models.Model):

    title = models.CharField(max_length=75)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    description = models.CharField(max_length=250)