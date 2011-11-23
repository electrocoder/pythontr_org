# -*- coding: utf-8-*-
# Projenin Adi : PythonTR-Türk Python' cular...
# Tarih : 2008-2011
# Yazar : pythontr.org ekibi
# Kontak : admin@pythontr.org
# Web : http://pythontr.org
# Python Versiyonu : 2.6-2.7
# Django Versiyonu : 1.2.5
# Amaci : www.pythontr.org sitesinin Django framework ile acik kaynakli kodlanmasi...
#         Eklemek isteginiz kodlar icin irtibat kurunuz...
#
#         http://pythontr.org
#
from myproject.polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)