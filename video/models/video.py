from django.db import models

from video.models import Category


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(to='video.Category', on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f'{self.title}'
