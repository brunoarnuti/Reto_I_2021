from django.contrib import admin
from bioinformatica.models.client import Client, Contact
from bioinformatica.models.logicaldelete import LogicalDeletedModelAdmin, LogicaLDeletedModelTabularInLine


class ClientInline(LogicaLDeletedModelTabularInLine):
    model = Client
    extra = 0
    classes = ['collapse']


class ContactInLine(LogicaLDeletedModelTabularInLine):
    model = Contact
    extra = 0
    classes = ['collapse']


class ClientAdmin(LogicalDeletedModelAdmin):
    list_display = ['name', 'address', 'phone', ]
    search_fields = ['name']
    inlines = [ContactInLine]
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Client Data', {'fields': ['address', ('phone', 'email')], 'classes': ['collapse']}),
    ]


class ContactAdmin(LogicalDeletedModelAdmin):
    list_display = ('name', 'last_name', 'phone', 'client')
    search_fields = ['name', 'last_name', 'client__name']


admin.site.register(Client, ClientAdmin)
admin.site.register(Contact, ContactAdmin)

