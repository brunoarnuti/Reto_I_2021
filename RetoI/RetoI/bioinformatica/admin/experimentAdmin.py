from django.contrib import admin
from bioinformatica.models.experiment import Experiment
from bioinformatica.admin.dinamicattributeAdmin import AttributeInline
from bioinformatica.admin.sampleAdmin import SamplesInline
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin


class ExperimentAdmin(LogicalDeletedModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Project id', {'fields': ['project_id']})
    ]

    list_display = ('name', 'place', 'state', 'project_id',)
    inlines = [SamplesInline, AttributeInline]
    list_filter = ['date']
    search_fields = ['name']


admin.site.register(Experiment, ExperimentAdmin)

