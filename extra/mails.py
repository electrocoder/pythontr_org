# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site

from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader

from pythontr_org.settings import ADMINS

FROM_EMAIL = 'yigitsadic@gmail.com'
TO = [ email for name, email in ADMINS ]


def ContactMail(form):
    """
        İletişim formu gönderildiğinde
        yöneticilere email gönderir.
    """
    
    subject = u'İletişim formu gönderildi.'
    
    c = Context({'form': form.clean()})
    
    html_content = (loader.get_template('emails/contact.html')).render(c)
    text_content = (loader.get_template('emails/contact.txt')).render(c)
    
    message = EmailMultiAlternatives(subject, text_content, FROM_EMAIL, TO)
    message.attach_alternative(html_content, 'text/html')
    
    return message


def AuthorMail(user):
    """
        Yazar olma isteği yapıldığında çalışır.
        
        Yöneticilere mail gönderir.
    """
    
    site = Site.objects.get_current()
    subject = u'Yazar olmak isteyen var!'

    c = Context({'user': user, 'site': site})
    
    html_content = (loader.get_template('emails/author.html')).render(c)
    text_content = (loader.get_template('emails/author.txt')).render(c)
    
    message = EmailMultiAlternatives(subject, text_content, FROM_EMAIL, TO)
    message.attach_alternative(html_content, 'text/html')
    
    return message    