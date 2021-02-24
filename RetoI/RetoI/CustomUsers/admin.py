from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    """
            Clase que extiende el UserAdmin, para de esta forma usar CustomUserCreationForms y poder
            asi crear CustomUsers
    """

    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('CI',)}),)
    fieldsets = (*UserAdmin.fieldsets, ('CI', {'fields': ('CI',)}))


admin.site.register(CustomUser, CustomUserAdmin)
