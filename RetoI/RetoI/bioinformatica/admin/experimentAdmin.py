from django.contrib import admin
from bioinformatica.models.experiment import Experiment
from bioinformatica.admin.sampleAdmin import SampleInline
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine
from bioinformatica.admin.dinamicattributeAdmin import DynamicAttributeInstanceInline


class ExperimentInline(LogicaLDeletedModelTabularInLine):
    model = Experiment
    extra = 0


class ExperimentAdmin(LogicalDeletedModelAdmin):
    fieldsets = [
        (None, {'fields': [('name','date'),('place','state')]}),
        ('Project', {'fields': ['project_id']})
    ]
    list_display = ('name','date','place','project_id','state')
    list_filter = ['date']
    search_fields = ['name','project_id']
    inlines = [DynamicAttributeInstanceInline,SampleInline]


admin.site.register(Experiment,ExperimentAdmin)

