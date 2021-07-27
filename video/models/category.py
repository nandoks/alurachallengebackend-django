from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.title
