from django.contrib import admin

from bioinformatica.models import DynamicAttributeInstance
from bioinformatica.models.experiment import Experiment

# Register your models here.

class AttributeInline(admin.TabularInline):
    model = DynamicAttributeInstance
    extra = 1

class ExperimentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['date']}),
        ('Project id', {'fields': ['project_id']})
    ]
    list_display = ('name','date','place','state','project_id',)
    list_filter = ['date']
    search_fields = ['name']
    inlines = [AttributeInline]

class experimentAdmin(admin.ModelAdmin):
    exclude = ['deleted', ]

admin.site.register(Experiment,ExperimentAdmin)

