from django.db import models
from .logicaldelete import LogicalDeletedModel

# Create your models here.

class FastQ(LogicalDeletedModel):
    sample = models.ForeignKey('Sample', on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField('date created', auto_now_add=True, editable=True)
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class FastQFile(models.Model):
    fastQ = models.ForeignKey(FastQ, on_delete=models.DO_NOTHING)
    file = models.FileField()

    def __str__(self):
        return self.fastQ.name
