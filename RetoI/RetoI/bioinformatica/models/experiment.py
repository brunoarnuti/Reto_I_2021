from django.db import models
from datetime import datetime
from .logicaldelete import LogicalDeletedModel
from django.utils.translation import gettext as _


class Experiment(LogicalDeletedModel):

    name = models.CharField(max_length=120)
    place = models.CharField(max_length=200)
    state = models.CharField(max_length=120)
    project_id = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(_('Date of experiment'), default=datetime.now())

    def __str__(self):
        return self.name

