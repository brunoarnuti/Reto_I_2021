from django.contrib import admin
from bioinformatica.models.sample import Sample


class SampleAdmin(admin.ModelAdmin):
    exclude = ['deleted', ]


admin.site.register(Sample, SampleAdmin)
