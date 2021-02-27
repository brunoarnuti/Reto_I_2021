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
        ('Project id', {'fields': ['project_id']}),
        ('Location',   {'fields':['location']})
    ]
    list_display = ('name','date','location','state','project_id')
    list_filter = ['date']
    search_fields = ['name']
    inlines = [AttributeInline]

class experimentAdmin(admin.ModelAdmin):
    exclude = ['deleted', ]

admin.site.register(Experiment,ExperimentAdmin)

