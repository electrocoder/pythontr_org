# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from pythontr_org.posts.models import Post, Category

from tinymce.widgets import TinyMCE

class PostForm(ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'
        
        self.fields['content'].widget.attrs['rows'] = 27
    
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        
    class Meta:
        model = Post
        
        exclude = ('created_at', 'updated_at', 'read_count', 'author', 'slug')