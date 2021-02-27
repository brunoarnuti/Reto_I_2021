from django.contrib import admin
from bioinformatica.models.sample import Sample
from bioinformatica.models.logicaldelete import LogicaLDeletedModelTabularInLine, LogicalDeletedModelAdmin


class SampleAdmin(LogicalDeletedModelAdmin):
     list_display = ('name','responsible','location')

class SampleInline(LogicaLDeletedModelTabularInLine):
    model = Sample
    extra = 0

admin.site.register(Sample, SampleAdmin)
