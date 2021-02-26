from django.db import models
from .logicaldelete import LogicalDeletedModel

# Create your models here.

class Fast5(LogicalDeletedModel):
    date_created = models.DateTimeField('date created', auto_now_add=True, editable=True)
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    name = models.CharField(max_length=240)


    def __str__(self):
        return self.name