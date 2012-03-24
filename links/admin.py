# -*- coding: utf-8 -*-

from django.contrib import admin

from pythontr_org.links.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'confirmed')
    search_fields = ['title', 'description']    
    date_hierarchy = 'created_at'
    
    list_filter = ('confirmed',)
    
    actions = ['confirm', 'unconfirm']
    
    
    def confirm(self, request, queryset):
        rows_updated = queryset.update(confirmed = True)
        
        self.message_user(request, u'%s bağlantı onaylandı!' % rows_updated)
    confirm.short_description = u'Seçili bağlantıları onayla'
    
        
    def unconfirm(self, request, queryset):
        rows_updated = queryset.update(confirmed = False)
        
        self.message_user(request, u'%s bağlantı reddedildi')
    unconfirm.short_description = u'Seçili bağlantıları reddet'
        

admin.site.register(Link, LinkAdmin)