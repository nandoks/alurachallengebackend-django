from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=100, )
    descricao = models.TextField()
    url = models.URLField()
