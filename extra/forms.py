# -*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'
    
    
    title = forms.CharField(label = u'Başlık')
    email = forms.EmailField()
    web_site = forms.URLField(initial = 'http://', required = False)
    content = forms.CharField(label = u'Mesaj içeriği', widget = forms.Textarea)