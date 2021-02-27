from django.contrib import admin
from bioinformatica.models.client import Client
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine
from bioinformatica.admin.projectAdmin import ProjectInline


class ClientInline(LogicaLDeletedModelTabularInLine):
    model = Client
    extra = 0

class clientAdmin(LogicalDeletedModelAdmin):
    inlines = [ProjectInline,ClientInline]
    exclude = ['project_ids','contact_ids']
    list_display = ('name','company','phone')


admin.site.register(Client,clientAdmin)
