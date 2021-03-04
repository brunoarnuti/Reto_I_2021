from django.db import models
from .logicaldelete import LogicalDeletedModel
from django.utils.translation import gettext as _
from RetoI.settings import UPLOAD_ROOT
import os


def get_upload_path(instance, filename):
    return os.path.join("%s/%s" % (UPLOAD_ROOT, filename))


class Fast5(LogicalDeletedModel):
    fast5_id = models.AutoField(primary_key=True)
    name = models.CharField(_('Name'), max_length=240)
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True, editable=True)
    file = models.FileField(upload_to=get_upload_path, verbose_name="Load fast5 File",
                            help_text='Seleccione El archivo Fast5', blank=True, null=True)
    experiment = models.ForeignKey(_('Experiment'), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Fast5, self).save(*args, **kwargs)
        filename = self.file.url
        print(self.file)
