from django.db import models


class JournalBlog(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
