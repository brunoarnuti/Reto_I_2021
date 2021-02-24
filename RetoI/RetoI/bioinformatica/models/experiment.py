from django.db import models
from django.utils import timezone

class Experiment(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField('date published',default=timezone.now)
    place = models.CharField(max_length=200)
    state = models.CharField(max_length=120)

    def __str__(self):
        return self.name
