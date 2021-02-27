from django.db import models
from .logicaldelete import LogicalDeletedModel


class Sample(LogicalDeletedModel):
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
    date_created = models.DateTimeField('date created', auto_now_add=True, editable=True)
    responsible = models.CharField(max_length=120)
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.experiment.name

