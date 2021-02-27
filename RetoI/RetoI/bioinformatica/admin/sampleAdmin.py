from django.contrib import admin
from bioinformatica.models.sample import Sample
from bioinformatica.models.logicaldelete import LogicaLDeletedModelTabularInLine, LogicalDeletedModelAdmin


class SampleAdmin(LogicalDeletedModelAdmin):
    search_fields = ['experiment__name', 'date_created', 'location']


class SamplesInline(LogicaLDeletedModelTabularInLine):
    model = Sample
    extra = 0


admin.site.register(Sample, SampleAdmin)
