from django.contrib import admin
from bioinformatica.models.fastQ import FastQ, FastQFile



class FastQAdmin(admin.ModelAdmin):
    exclude = ['deleted', ]


admin.site.register(FastQ, FastQAdmin)
