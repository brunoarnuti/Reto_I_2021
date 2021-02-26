from django.contrib import admin
from bioinformatica.models.client import Client


class clientAdmin(admin.ModelAdmin):
    exclude = ['deleted', ]


admin.site.register(Client)
