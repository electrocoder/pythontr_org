# -*- coding: utf-8 -*-

from django.contrib import admin

from pythontr_org.links.models import Link

class LinkAdmin(admin.ModelAdmin):    
    list_display = ('title', 'href', 'confirmed')
    search_fields = ['title', 'description']    
    date_hierarchy = 'created_at'
    
    list_filter = ('confirmed',)
    
    
admin.site.register(Link, LinkAdmin)