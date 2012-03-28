# -*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'
    
    
    title = forms.CharField(label=u'Başlık')
    email = forms.EmailField()
    web_site = forms.URLField(initial='http://', required=False)
    content = forms.CharField(label=u'Mesaj içeriği', widget=forms.Textarea)
    

CHOICES = (
           ('Web programlama', 'Web programlama'),
           ('GUI programlama', 'GUI programlama'),
           (u'Sistem yönetimi', u'Sistem yönetimi'),
           (u'Veritabanı sistemleri', u'Veritabanı sistemleri'),
           (u'İşletim sistemleri', u'İşletim sistemleri'),
)    

    
class AuthorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'


    focused_on = forms.MultipleChoiceField(
                                 label=u'Yöneliminiz',
                                 choices=CHOICES,
                                 help_text='Genel olarak hangi konular üzerinde yazabilirsiniz?'
                                 )
                
    projects = forms.CharField(
                               label=u'Projeler',
                               widget=forms.Textarea(),
                               required=False,
                               help_text='Lütfen adreslerini de yazınız.'
                               )
    
    extra_info = forms.CharField(
                                 label=u'Extra',
                                 widget=forms.Textarea(),
                                 required=False,
                                 help_text='Başka bildirmek istediğiniz şeyler'
                                 )