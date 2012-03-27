# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site

from django.core.mail import send_mail
from django.template import Context, loader

from pythontr_org.settings import ADMINS, FROM_EMAIL

TO = [ email for name, email in ADMINS ]


def ContactMail(form):
    c = Context({'form': form.clean()})
    subject = u'İletişim formu gönderildi.'
    
    html_content = (loader.get_template('main/mails/contact.txt')).render(c)
    
    send_mail(subject, html_content, FROM_EMAIL, TO)


def AuthorMail(user):
    site = Site.objects.get_current()
    subject = u'Yazar olmak isteyen var!'

    c = Context({'user': user, 'site': site})
    
    html_content = (loader.get_template('main/mails/author.txt')).render(c)
    
    send_mail(subject, html_content, FROM_EMAIL, TO)