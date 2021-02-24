from django.db import models


# Create your models here.

class Sample(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
    date_created = models.DateTimeField('date created', auto_now_add=True, editable=True)
    technician = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name