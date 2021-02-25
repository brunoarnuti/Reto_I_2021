from django.contrib import admin
from bioinformatica.models.project import Project
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin


class ProjectAdmin(LogicalDeletedModelAdmin):
    list_display = ('name','contact','create_date')
    list_filter = ['name','contact','create_date']
    search_fields = ['name','contact__name', 'contact__surname',]



admin.site.register(Project,ProjectAdmin)








