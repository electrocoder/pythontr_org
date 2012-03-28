# -*- coding: utf-8 -*-

from django.core.mail import send_mail, send_mass_mail
from django.template import Context, loader

from pythontr_org.settings import ADMINS, FROM_EMAIL
from django.contrib.sites.models import Site

TO = [ email for name, email in ADMINS ]


def accept_author_requests_mail(user):    
    subject = u'Yazar olma isteğin onaylandı.'
    site    = Site.objects.get_current() 
    
    c = Context({'user': user, 'site': site})
    message = (loader.get_template('users/mails/author_request_accepted.txt')).render(c)
    
    send_mail(subject, message, FROM_EMAIL, [user.email], True)


def decline_author_requests_mail(user):
    subject = u'Yazar olma isteğin reddedildi.'    
    c       = Context({'user': user})
    message =  (loader.get_template('users/mails/author_request_declined.txt')).render(c)
    
    send_mail(subject, message, FROM_EMAIL, [user.email], True)
    
    
def invite_friend_mail(user, formset):
    subject  = u'pythontr.org bilginin paylaşıldığı yer'
    messages = []
    
    for form in formset:
        if form:
            c       = Context({'user': user, 'form': form, 'site': Site.objects.get_current()})
            message = (loader.get_template('users/mails/invite_friend_mail.txt')).render(c)
            
            messages.append([subject, message, FROM_EMAIL, [form['email']]])
            
    send_mass_mail(messages, fail_silently=True)
    
def user_signed_up(user):
    subject = u'Üye kayıt oldu'
    site = Site.objects.get_current()
    
    c = Context({'user': user, 'site': site})
    
    message = (loader.get_template('users/mails/user_signed_up.txt')).render(c)
    
    send_mail(subject, message, FROM_EMAIL, TO)