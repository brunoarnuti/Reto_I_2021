import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from .logicaldelete import LogicalDeletedModel
from RetoI.settings import UPLOAD_ROOT
from django.utils.translation import gettext as _


class FastQ(LogicalDeletedModel):
    fastQ_id = models.AutoField(primary_key=True)
    name = models.CharField(_('Name'), max_length=240)
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True, editable=True)
    experiment = models.ForeignKey(_('Experiment'), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class UploadRootStorage(FileSystemStorage):
    def __init__(self):
        """Create the storage."""
        FileSystemStorage.__init__(self,
                                   location=UPLOAD_ROOT,
                                   base_url='/'
                                   )


def get_upload_path(instance, filename):
    return os.path.join("%s/%s" % (UPLOAD_ROOT, filename))


class FastQFile(LogicalDeletedModel):
    fastQ = models.ForeignKey(FastQ, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=get_upload_path, verbose_name="Load fastQ File",
                            help_text='Seleccione El archivo FastQ')

    def __str__(self):
        return self.fastQ.name

    def save(self, *args, **kwargs):
        super(FastQFile, self).save(*args, **kwargs)
        filename = self.file.url
        print(self.file)
