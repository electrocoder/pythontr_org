# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site

from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader

from pythontr_org.settings import ADMINS

FROM_EMAIL = 'yigitsadic@gmail.com'
TO = [ email for name, email in ADMINS ]


def LinkAddedMail(link):
    """
        Yeni bağlantı eklendiğinde yöneticilere
        email gönderir.
    """
    
    site = Site.objects.get_current()
    subject = u'Yeni bağlantı eklendi.'
    
    c = Context({'link': link, 'site': site})
    
    html_content = (loader.get_template('emails/link_added.html')).render(c)
    text_content = (loader.get_template('emails/link_added.txt')).render(c)
    
    message = EmailMultiAlternatives(subject, text_content, FROM_EMAIL, TO)
    message.attach_alternative(html_content, 'text/html')
    
    return message
