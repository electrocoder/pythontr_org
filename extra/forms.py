# -*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    
    
    title = forms.CharField()
    email = forms.EmailField(required = False)
    web_site = forms.URLField(required = False)
    content = forms.CharField(widget = forms.Textarea)