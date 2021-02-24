from django.contrib import admin

from bioinformatica.models import DynamicAttribute
from bioinformatica.models.experiment import Experiment

# Register your models here.

class AttributeInline(admin.TabularInline):
    model = DynamicAttribute
    extra = 1

class ExperimentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['date']}),
        ('Project id', {'fields': ['project_id']})
    ]
    list_display = ('name','date','place','state','project_id')
    list_filter = ['date']
    search_fields = ['name']
    inlines = [AttributeInline]

admin.site.register(Experiment,ExperimentAdmin)

