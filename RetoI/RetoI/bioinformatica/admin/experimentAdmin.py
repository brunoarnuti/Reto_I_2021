from django.contrib import admin
from bioinformatica.models.experiment import Experiment
# Register your models here.

class ExperimentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                    {'fields': ['name']}),
        ('Date information',      {'fields': ['date']})
    ]
    list_display = ('name','date','place','state')
    list_filter = ['date']
    search_fields = ['name']

admin.site.register(Experiment,ExperimentAdmin)
