from myproject.pythonauthors.models import PythonAuthors
from django.contrib import admin

class PythonAuthorsAdmin(admin.ModelAdmin):
    fields=[
            'pythonauthors_name',
            'pythonauthors_photo',
            'pythonauthors_web',
            'pythonauthors_email',
            'pythonauthors_content'            ]
    
    search_fields=list_display=('pythonauthors_name', 'pythonauthors_web',)

admin.site.register(PythonAuthors, PythonAuthorsAdmin)
