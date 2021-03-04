from django.contrib import admin
from bioinformatica.models.sample import Sample
from bioinformatica.models.logicaldelete import LogicaLDeletedModelTabularInLine, LogicalDeletedModelAdmin
from bioinformatica.admin.fastQAdmin import FastQInline


class SampleAdmin(LogicalDeletedModelAdmin):
    search_fields = ['experiment__name', 'date_created', 'location']
    list_display = ('sample_id', 'experiment', 'responsible', 'location')
    inlines = [FastQInline]


class SamplesInline(LogicaLDeletedModelTabularInLine):
    model = Sample
    extra = 0


admin.site.register(Sample, SampleAdmin)
