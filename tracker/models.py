from django.db import models


class TrackerApp(models.Model):
    weight = models.FloatField()
    neck = models.FloatField()
    arms = models.FloatField()
    forearms = models.FloatField()
    wrist = models.FloatField()
    chest = models.FloatField()
    stomach = models.FloatField()
    waist = models.FloatField()
    butt = models.FloatField()
    thighs = models.FloatField()
    calves = models.FloatField()
