from myproject.pythoncoders.models import PythonCoders
from django.contrib import admin

class PythonCodersAdmin(admin.ModelAdmin):
    fields=[
            'pythoncoders_name',
            'pythoncoders_photo',
            'pythoncoders_web',
            'pythoncoders_email',
            'pythoncoders_bio',
            'pythoncoders_school',
            'pythoncoders_job',
            'pythoncoders_git',
            'pythoncoders_mobil',
            'pythoncoders_star',
            'pythoncoders_pubdate'
            ]
    
    search_fields=list_display=('pythoncoders_name', 'pythoncoders_web',)

admin.site.register(PythonCoders, PythonCodersAdmin)
