from django.db import models

from video.models import Category


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return f'{self.title}'
