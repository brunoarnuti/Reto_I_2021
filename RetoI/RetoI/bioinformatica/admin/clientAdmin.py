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
    fieldsets = [
        (None, {'fields': [('name','surname')]}),
        ('Other information', {'fields': [('direction','company'),('phone','email')],'classes':['collapse']}),
    ]


admin.site.register(Client, clientAdmin)
