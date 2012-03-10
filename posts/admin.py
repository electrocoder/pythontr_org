from myproject.python.models import Posts, Categories, Authors
from django.contrib import admin

class CategoriesAdmin(admin.ModelAdmin):
    fields=[
            'category_name'
            ]
    
    search_fields=list_display=('category_name',)
    
class AuthorsAdmin(admin.ModelAdmin):
    fields=[
            'author_name',
            'author_photo',
            'author_web',
            'author_email',
            'author_bio'
            ]
    
    search_fields=list_display=('author_name','author_photo', 'author_web', 'author_email', 'author_bio',)

class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'post_link': ('post_title', )}
    fields=[
            'post_author',
            'post_title',
            'post_link',
            'post_body',
            'post_category',
            'post_pubdate',
            'post_update',
            'post_publish',
            'post_tags',
            'post_read_count',
            'post_star'
            ]
    
    #list_display=('post_author', 'post_title', 'post_link', 'post_category', 'post_pubdate', 'post_update', 'post_tags', 'post_publish', 'post_read_count', 'post_star',)
    search_fields=list_display=('post_title', 'post_pubdate', 'post_publish', 'post_read_count', 'post_star',  'post_tags',)
    list_filter=('post_author', 'post_category', 'post_publish', 'post_star',)
    date_hierarchy='post_pubdate'

admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Posts, PostsAdmin)
