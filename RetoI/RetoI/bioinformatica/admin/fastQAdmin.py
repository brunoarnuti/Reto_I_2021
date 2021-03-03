from django.contrib import admin
from bioinformatica.models.fastQ import FastQ, FastQFile

from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin


class FastQAdmin(LogicalDeletedModelAdmin):
    search_fields = ['date_created']


class FastQFileAdmin(LogicalDeletedModelAdmin):
    pass


admin.site.register(FastQ, FastQAdmin)
admin.site.register(FastQFile, FastQFileAdmin)
