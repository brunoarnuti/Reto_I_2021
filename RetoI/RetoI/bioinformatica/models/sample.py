from django.db import models
from .logicaldelete import LogicalDeletedModel
from django.utils.translation import gettext as _


# Create your models here.

class Sample(LogicalDeletedModel):

    experiment = models.ForeignKey(_('Experiment'), on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True, editable=True)
    responsible = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    name = models.CharField(_('Name'),max_length=120, blank=True,null=True)

    def __str__(self):
        return self.experiment.name
