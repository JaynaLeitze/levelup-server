from django.db import models

class Event(models.Model):

    scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=75)

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value