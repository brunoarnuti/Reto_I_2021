from django.contrib import admin
from bioinformatica.models.client import Client
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin


class clientAdmin(LogicalDeletedModelAdmin):
    exclude = ['deleted', ]


admin.site.register(Client,clientAdmin)
