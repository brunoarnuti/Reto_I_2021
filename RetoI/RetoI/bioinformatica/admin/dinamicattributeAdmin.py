from django.contrib import admin
from bioinformatica.models.dinamicattribute import DynamicAttributeDefinition, DynamicAttributeInstance
from bioinformatica.models.logicaldelete import LogicaLDeletedModelTabularInLine, LogicalDeletedModelAdmin


class DynamicAttributeInstanceInline(LogicaLDeletedModelTabularInLine):
    model = DynamicAttributeInstance
    extra = 0


class AttributeDefinitionInline(LogicaLDeletedModelTabularInLine):
    model = DynamicAttributeDefinition
    extra = 0


class DynamicAttributeDefinitionAdmin(LogicalDeletedModelAdmin):
    fieldsets = [
        ('Name',                    {'fields': ['attribute_name']}),
        ('Description',             {'fields': ['attribute_description']}),
    ]
    list_display = ('attribute_name', 'attribute_description')
    search_fields = ['attribute_name']


class DynamicAttributeAdmin(LogicalDeletedModelAdmin):
    fieldsets = [
        (None, {'fields': ['attribute_type']}),
        ('Value', {'fields': ['attribute_value']}),
    ]


admin.site.register(DynamicAttributeDefinition, DynamicAttributeDefinitionAdmin)

