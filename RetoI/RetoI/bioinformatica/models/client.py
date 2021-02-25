from django.db import models
from django.utils.translation import gettext as _
from .project import Project

class Client(models.Model):

    name = models.CharField(_('Name'), max_length=200)
    surname = models.CharField(_('Surname'), max_length=200)
    company = models.CharField(_('Company'), max_length=200, blank=True)
    direction = models.CharField(_('Direction'), max_length=200)
    email = models.CharField('E-mail', max_length=200, blank=True)
    phone = models.CharField(_('Phone'), max_length=200)
    project_ids = models.ManyToManyField(Project, blank=True)
    contact_ids = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

