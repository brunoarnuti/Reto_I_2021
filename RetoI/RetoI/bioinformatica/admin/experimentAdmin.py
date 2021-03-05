from admin_confirm.admin import confirm_action, AdminConfirmMixin
from django.contrib import admin
from bioinformatica.models.experiment import Experiment
from bioinformatica.admin.dinamicattributeAdmin import AttributeInline
from bioinformatica.admin.sampleAdmin import SamplesInline
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine
from django.core.management import call_command
import redis_lock
import time
from django.contrib import messages
from bioinformatica.admin.fastQAdmin import FastQInline
from bioinformatica.admin.fast5Admin import Fast5Inline


class ExperimentAdmin(AdminConfirmMixin, LogicalDeletedModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'executionCommands']}),
        ('Project id', {'fields': ['project_id']})
    ]

    confirm_change = True
    confirm_add = True
    confirmation_fields = ['name', 'project_id']

    actions = ["experiment_actions"]

    @confirm_action
    def experiment_actions(self, obj, queryset=[]):
        for q in queryset:
            conn = redis_lock.StrictRedis(host='67.205.171.138', port=6379)
            lock = redis_lock.Lock(conn, "exprimento" + str(q.pk))
            if lock.acquire(timeout=1):
                print(f"Tomando experimento nro: {q.pk}")
                time.sleep(20)
                call_command("experimentCommand", q.executionCommands, q.name, experiment_id=q.experiment_id)
                lock.release()
            else:
                messages.add_message(obj, messages.INFO, 'Alguien ya está trabajando con este experimento')

    # confirm_action(experiment_actions)
    experiment_actions.allowed_permissions = ('change',)

    experiment_actions.short_description = 'RUN'
    experiment_actions.allow_tags = True
    list_display = ('name', 'location', 'state', 'project_id', 'experiment_actions')
    inlines = [SamplesInline, AttributeInline]
    list_filter = ['date']
    search_fields = ['name']


admin.site.register(Experiment, ExperimentAdmin)


class ExperimentInline(LogicaLDeletedModelTabularInLine):
    model = Experiment
    extra = 0
    classes = ['collapse']
