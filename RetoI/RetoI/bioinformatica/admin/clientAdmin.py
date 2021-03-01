from django.contrib import admin
from bioinformatica.models.client import Client
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine
from bioinformatica.admin.projectAdmin import ProjectInline


class ClientInline(LogicaLDeletedModelTabularInLine):
    model = Client
    extra = 0
    classes = ['collapse']

class clientAdmin(LogicalDeletedModelAdmin):
    search_fields = ['name', 'surname']
    inlines = [ClientInline,ProjectInline]


admin.site.register(Client, clientAdmin)
