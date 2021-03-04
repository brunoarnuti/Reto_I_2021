from django.contrib import admin
from bioinformatica.models.fast5 import Fast5
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine


class Fast5Inline(LogicaLDeletedModelTabularInLine):
    model = Fast5
    extra = 0
    classes = ['collapse']


class Fast5Admin(LogicalDeletedModelAdmin):
    search_fields = ['date_created']


class Fast5FileAdmin(LogicalDeletedModelAdmin):
    pass


admin.site.register(Fast5, Fast5Admin)
