from django.db import models
from .logicaldelete import LogicalDeletedModel


# Create your models here.

class Sample(LogicalDeletedModel):
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
    date_created = models.DateTimeField('date created', auto_now_add=True, editable=True)
    technician = models.CharField(max_length=120)
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.experiment.name