from django.contrib import admin
from bioinformatica.models.project import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','contact','create_date')
    list_filter = ['name','contact','create_date']
    search_fields = ['name','contact__name']

admin.site.register(Project,ProjectAdmin)







