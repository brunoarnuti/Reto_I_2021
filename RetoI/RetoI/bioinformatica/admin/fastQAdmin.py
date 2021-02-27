from django.contrib import admin
from bioinformatica.models.fastQ import FastQ, FastQFile
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin


class FastQAdmin(LogicalDeletedModelAdmin):
    pass

admin.site.register(FastQ, FastQAdmin)
