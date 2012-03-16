# -*- coding: utf-8 -*-

from django.contrib import admin

from pythontr_org.links.models import Link

class LinkAdmin(admin.ModelAdmin):    
    list_display = ('title', 'href')
    search_fields = ['title', 'description']    
    date_hierarchy = 'created_at'
    
    
admin.site.register(Link, LinkAdmin)