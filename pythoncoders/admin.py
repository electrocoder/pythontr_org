from myproject.pythoncoders.models import PythonCoders
from django.contrib import admin

class PythonCodersAdmin(admin.ModelAdmin):
    fields=[
            'pythoncoders_name',
            'pythoncoders_photo',
            'pythoncoders_web',
            'pythoncoders_email',
            'pythoncoders_bio',
<<<<<<< HEAD
            'pythoncoders_school',
            'pythoncoders_job',
            'pythoncoders_git',
            'pythoncoders_mobil',
            'pythoncoders_star',
            'pythoncoders_pubdate'
=======
            'pythoncoders_git',
            'pythoncoders_mobil',
            'pythoncoders_star'
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
            ]
    
    search_fields=list_display=('pythoncoders_name', 'pythoncoders_web',)

admin.site.register(PythonCoders, PythonCodersAdmin)
