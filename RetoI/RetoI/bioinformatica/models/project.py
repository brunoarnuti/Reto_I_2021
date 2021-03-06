from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from .logicaldelete import LogicalDeletedModel


class Project(LogicalDeletedModel):

    name = models.CharField(_('Name'), max_length=200)
    create_date = models.DateTimeField(_('Create date'), default=datetime.now())
    description = models.TextField(_('Description'), blank=True)
    contact = models.ForeignKey('Client', on_delete=models.DO_NOTHING)
    projects = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


