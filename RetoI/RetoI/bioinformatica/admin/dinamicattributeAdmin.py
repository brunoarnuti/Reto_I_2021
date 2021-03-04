from django.contrib import admin
from bioinformatica.models.dinamicattribute import DynamicAttributeDefinition
from bioinformatica.models.dinamicattribute import DynamicAttributeInstance
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine


class AttributeInline(LogicaLDeletedModelTabularInLine):
    model = DynamicAttributeInstance
    extra = 1
    fields = ['attribute_type', 'attribute_value']


class DynamicAttributeDefinitionAdmin(LogicalDeletedModelAdmin):
    list_display = ('attribute_name', 'attribute_description')
    search_fields = ['attribute_name']


class DynamicAttributeInstanceAdmin(LogicalDeletedModelAdmin):
    fieldsets = [
        (None, {'fields': ['attribute_type']}),
        ('Value', {'fields': ['attribute_value']}),
    ]


admin.site.register(DynamicAttributeDefinition, DynamicAttributeDefinitionAdmin)
admin.site.register(DynamicAttributeInstance, DynamicAttributeInstanceAdmin)
