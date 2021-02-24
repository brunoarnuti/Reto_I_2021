from django.db import models
from django.utils.translation import gettext as _

class Client(models.Model):

    name = models.CharField(_('Name'), max_length=200)
    surname = models.CharField(_('Surname'), max_length=200)
    direction = models.CharField(_('Direction'), max_length=200)
    email = models.CharField('E-mail', max_length=200)
    phone = models.CharField(_('Phone'), max_length=200)
    project_ids = models.ForeignKey('Project', on_delete=models.DO_NOTHING)
    contact_ids = models.ForeignKey('Client', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

