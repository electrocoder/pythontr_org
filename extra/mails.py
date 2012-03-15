# -*- coding: utf-8 -*-

from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader

FROM_EMAIL = 'yigitsadic@gmail.com'
TO = 'yigitsadic@gmail.com'

def ContactMail(form):
    """
        İletişim formu gönderildiğinde
        yöneticilere email gönderir.
    """
    
    subject = u'İletişim formu gönderildi.'
    
    
    t = loader.get_template('mails/contact.html')
    c = Context({'form': form.clean()})
    
    
    html_content = t.render(c)
    text_content = u"""
    İletişim formu gönderildi.
    ----
    İçerik;
    Başlık: %s
    Email: %s
    Website: %s
    Mesaj içerik:
        %s    
    """ % (form.cleaned_data['title'], form.cleaned_data['email'], form.cleaned_data['web_site'], form.cleaned_data['content'])
    
    
    message = EmailMultiAlternatives(subject, text_content, FROM_EMAIL, [TO])
    message.attach_alternative(html_content, 'text/html')
    
    return message


def AuthorMail(user):
    """
        Yazar olma isteği yapıldığında çalışır.
        
        Yöneticilere mail gönderir.
    """
    
    subject = u'Yazar olmak isteyen var!'
    
    t = loader.get_template('mails/author.html')
    c = Context({'user': user})
    
    html_content = t.render(c)
    text_content = u"""
    Yazar olmak isteyen var.
    ----
    Üye: %s
    Admin sayfa linki: http://pythontr.org/admin/auth/user/%s/
    
    """ % (user, user.id)
    
    message = EmailMultiAlternatives(subject, text_content, FROM_EMAIL, [TO])
    message.attach_alternative(html_content, 'text/html')
    
    return message
    
    