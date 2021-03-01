from django.contrib import admin
from bioinformatica.models.client import Client
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine


class ClientInline(LogicaLDeletedModelTabularInLine):
    model = Client
    extra = 0
    classes = ['collapse']

class clientAdmin(LogicalDeletedModelAdmin):
    search_fields = ['name', 'surname']
    inlines = [ClientInline] #agregar projectInLines


admin.site.register(Client, clientAdmin)
