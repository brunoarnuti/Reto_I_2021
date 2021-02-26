from django.contrib import admin
from bioinformatica.models.dinamicattribute import DynamicAttribute
# Register your models here.


class DinamicAttributeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Id',                    {'fields': ['attribute_id']}),
        ('Type',                  {'fields': ['attribute_type']}),
        ('Value',                 {'fields': ['attribute_value']})

    ]
    list_display = ('attribute_id', 'attribute_type', 'attribute_value')
    search_fields = ['attribute_id']

admin.site.register(DynamicAttribute, DinamicAttributeAdmin)