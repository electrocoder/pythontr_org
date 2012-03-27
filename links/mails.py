# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site

from django.core.mail import send_mail
from django.template import Context, loader

from pythontr_org.settings import ADMINS, FROM_EMAIL


TO = [ email for name, email in ADMINS ]


def LinkAddedMail(link):
    """
        Yeni bağlantı eklendiğinde yöneticilere
        email gönderir.
    """
    
    site = Site.objects.get_current()
    subject = u'Yeni bağlantı eklendi.'
    
    c = Context({'link': link, 'site': site})    
    html_content = (loader.get_template('links/mails/link_added.txt')).render(c)
    
    send_mail(subject, html_content, FROM_EMAIL, TO)