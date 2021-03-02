from django.contrib import admin
from bioinformatica.models.experiment import Experiment
from bioinformatica.admin.dinamicattributeAdmin import AttributeInline
from bioinformatica.admin.sampleAdmin import SamplesInline
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine
from django.urls import path, reverse
from django.utils.html import format_html
<<<<<<< HEAD
from django.urls import reverse
=======
>>>>>>> d5a7bc0e7eefcbe4731b8bfde5b71fbb6facf2a4
from django.core.management import call_command


class ExperimentAdmin(LogicalDeletedModelAdmin):

    fieldsets = [
        (None, {'fields': ['name','executionCommands']}),
        ('Project id', {'fields': ['project_id']})
    ]

    def experiment_actions(self, obj,queryset=[]):
        for q in queryset:
            print(q.id)
            call_command("experimentCommand", q.executionCommands,q.name,experiment_id = q.id)



    actions = ['experiment_actions']
    experiment_actions.short_description = 'RUN'
    experiment_actions.allow_tags = True

    list_display = ('name', 'location', 'state', 'project_id','experiment_actions')
    inlines = [SamplesInline, AttributeInline]
    list_filter = ['date']
    search_fields = ['name']


admin.site.register(Experiment, ExperimentAdmin)

class ExperimentInline(LogicaLDeletedModelTabularInLine):
    model = Experiment
    extra = 0
    classes = ['collapse']

