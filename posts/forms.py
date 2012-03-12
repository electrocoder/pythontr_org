# -*- coding: utf-8 -*-

from django.forms import ModelForm

from pythontr_org.posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        
        exclude = ('created_at', 'updated_at', 'read_count', 'author')