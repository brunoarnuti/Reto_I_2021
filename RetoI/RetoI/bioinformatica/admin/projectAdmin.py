from django.contrib import admin
from bioinformatica.models.project import Project
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin
from bioinformatica.admin.experimentAdmin import ExperimentInline
from bioinformatica.models.logicaldelete import LogicaLDeletedModelTabularInLine


class ProjectInline(LogicaLDeletedModelTabularInLine):
    model = Project
    extra = 0

class ProjectAdmin(LogicalDeletedModelAdmin):
    list_display = ('name','contact','create_date')
    list_filter = ['create_date']
    search_fields = ['name','contact__name', 'contact__surname',]
    inlines = [ExperimentInline,ProjectInline]

    fieldsets = [
        (None, {'fields': [('name','contact')]}),
        ('Project information', {'fields': ['create_date','description','projects'],'classes':['collapse']}),
    ]

admin.site.register(Project,ProjectAdmin)

