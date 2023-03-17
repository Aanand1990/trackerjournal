from django.db import models


class EODChecklist(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    gym_workout = models.BooleanField(default=False)
    reading_50_pages = models.BooleanField(default=False)
    coding_half_hour = models.BooleanField(default=False)
    quality_sleep = models.BooleanField(default=False)

