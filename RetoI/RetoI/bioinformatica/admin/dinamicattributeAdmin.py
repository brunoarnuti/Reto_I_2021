from django.contrib import admin
from bioinformatica.models.dinamicattribute import DynamicAttributeDefinition
from bioinformatica.models.dinamicattribute import DynamicAttributeInstance
# Register your models here.


class AttributeDefinitionInline(admin.TabularInline):
    model = DynamicAttributeDefinition
    extra = 1


class DynamicAttributeDefinitionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                    {'fields': ['attribute_name']}),
        ('Description',             {'fields': ['attribute_description']}),
    ]
    list_display = ('attribute_name', 'attribute_description')
    search_fields = ['attribute_name']


class DynamicAttributeAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['attribute_type']}),
        ('Value', {'fields': ['attribute_value']}),
    ]


admin.site.register(DynamicAttributeDefinition, DynamicAttributeDefinitionAdmin)

