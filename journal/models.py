from django.db import models

class JournalBlog(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.TextField()

