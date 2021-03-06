# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from pythontr_org.posts.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields       = ['name']
    prepopulated_fields = {'slug': ('name', )}


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
                 (u'Yazar ve kategori bilgileri',
                  {
                    'fields': ('author', 'category')
                  }),
                 (u'Başlık ve içerik',
                  {
                    'fields': ('title', 'slug', 'content')
                 }),
                 (u'Yayınlanma bilgileri',
                  {
                    'fields': ('published', 'tags', 'read_count')
                  })
    )
    
    save_on_top = True
    prepopulated_fields = {'slug': ('title', )}
    
    list_display  = ('title', 'category', 'author', 'published', 'read_count', 'created_at')    
    search_fields = ['title', 'content', 'tags']    
    list_filter   = ('published', 'category', 'author')
    
    date_hierarchy = 'created_at'
    
    # admin actions
    
    actions = ['publish', 'unpublish']
    
    def publish(self, request, queryset):
        rows_updated = queryset.update(published = True)
        
        self.message_user(request, u"%s gönderi başarı ile yayınlandı!" % rows_updated)
    publish.short_description = u'Seçili gönderileri yayınla'
    
    
    def unpublish(self, request, queryset):
        rows_updated = queryset.update(published = False)
        
        self.message_user(request, u"%s gönderi başarı ile yayından kaldırıldı!" % rows_updated)
    unpublish.short_description = u'Seçili gönderileri yayından kaldır'
    
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=forms.Textarea(
                attrs={'cols': 100, 'rows': 30},
            ))
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)