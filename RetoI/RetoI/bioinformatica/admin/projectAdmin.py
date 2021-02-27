from django.contrib import admin
from bioinformatica.models.project import Project
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine
from bioinformatica.models.experiment import Experiment


class AttributeInlineExperiment(LogicaLDeletedModelTabularInLine):
    model = Experiment
    extra = 0
    classes = ['collapse']


class AttributeInlineProject(LogicaLDeletedModelTabularInLine):
    model = Project
    extra = 0
    classes = ['collapse']


class ProjectAdmin(LogicalDeletedModelAdmin):

    list_display = ('name', 'contact', 'create_date')

    list_filter = ['name', 'contact', 'create_date']

    search_fields = ['name', 'contact__name', 'contact__surname']

    inlines = [AttributeInlineExperiment, AttributeInlineProject]


    fieldsets = [
        (None, {'fields': [('name','contact')]}),
        ('Project information', {'fields': ['create_date','description','projects'],'classes':['collapse']}),
    ]

class projectAdmin(LogicalDeletedModelAdmin):
    pass


admin.site.register(Project,ProjectAdmin)

