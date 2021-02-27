from django.db import models
from django.utils import timezone
from .logicaldelete import LogicalDeletedModel
import logging

logger = logging.getLogger(__name__)

class Experiment(LogicalDeletedModel):
    name = models.CharField(max_length=120)
    date = models.DateTimeField('date published', default=timezone.now)
    location = models.CharField(max_length=200)
    state = models.CharField(max_length=120)
    project_id = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=True, null=True)
    logger.info("[INFO] Primer log")

    def __str__(self):
        return self.name
