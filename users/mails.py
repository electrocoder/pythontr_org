# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.template import Context, loader

from pythontr_org.settings import ADMINS, FROM_EMAIL
from django.contrib.sites.models import Site

TO = [ email for name, email in ADMINS ]


def accept_author_requests_mail(user):    
    subject = u'Yazar olma isteğin onaylandı.'
    site    = Site.objects.get_current() 
    
    c = Context({'user': user, 'site': site})
    html_content = (loader.get_template('users/mails/author_request_accepted.txt')).render(c)
    
    send_mail(subject, html_content, FROM_EMAIL, [user.email], True)


def decline_author_requests_mail(user):
    subject      = u'Yazar olma isteğin reddedildi.'    
    c            = Context({'user': user})
    html_content =  (loader.get_template('users/mails/author_request_declined.txt')).render(c)
    
    send_mail(subject, html_content, FROM_EMAIL, [user.email], True)