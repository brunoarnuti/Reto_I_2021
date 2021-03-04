from django.db import models
from .logicaldelete import LogicalDeletedModel
from django.utils.translation import gettext as _


class Sample(LogicalDeletedModel):
    sample_id = models.AutoField(primary_key=True)
    experiment = models.ForeignKey(_('Experiment'), on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True, editable=True)
    responsible = models.CharField(_('Responsible'), max_length=120)
    location = models.CharField(_('Location'), max_length=120)

    def __str__(self):
        return self.experiment.name
