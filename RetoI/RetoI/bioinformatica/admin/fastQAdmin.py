from django.contrib import admin
from bioinformatica.models.fastQ import FastQ, FastQFile
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine


class FastQFileAdmin(LogicalDeletedModelAdmin):
    list_display = ('fastQ', 'file')


class FastQFileInline(LogicaLDeletedModelTabularInLine):
    model = FastQFile
    extra = 0
    classes = ['collapse']


class FastQInline(LogicaLDeletedModelTabularInLine):
    model = FastQ
    extra = 0
    classes = ['collapse']


class FastQAdmin(LogicalDeletedModelAdmin):
    search_fields = ['date_created']
    inlines = [FastQFileInline]
    list_display = ('fastQ_id', 'name', 'sample')


admin.site.register(FastQ, FastQAdmin)
admin.site.register(FastQFile, FastQFileAdmin)
