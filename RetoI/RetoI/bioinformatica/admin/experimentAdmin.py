from django.contrib import admin
from bioinformatica.models.experiment import Experiment
from bioinformatica.admin.dinamicattributeAdmin import AttributeInline
from bioinformatica.admin.sampleAdmin import SamplesInline
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine
from django.urls import path, reverse
from django.utils.html import format_html


class ExperimentAdmin(LogicalDeletedModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Project id', {'fields': ['project_id']})
    ]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:experiment_id>/run/',
                self.admin_site.admin_view(self.experiment_run),
                name='experiment-run',
            ),

        ]
        return custom_urls + urls

    def experiment_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Run</a>&nbsp;',
            reverse('admin:experiment-run', args=[obj.id]),
        )

    def experiment_run(self, request, experiment_id, *args):
        from django.core.management import call_command
        call_command("experimentCommand", experiment_id)

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

