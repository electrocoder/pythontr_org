# -*- coding: utf-8 -*-

from pythontr_org.posts.models import Post, Category, Author
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    
    
    search_fields = ['name']


    
class AuthorAdmin(admin.ModelAdmin):
    
    
    search_fields = ['user', 'web_site', 'about']    
    list_display = ('user', 'web_site')



class PostAdmin(admin.ModelAdmin):
    
    
    prepopulated_fields = {'slug': ('title', )}
    
    list_display = ('title', 'published', 'created_at')    
    search_fields = ['title', 'content']    
    list_filter = ('published', )
    
    date_hierarchy = 'created_at'

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)