# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from pythontr_org.extra.forms import ContactForm, AuthorForm

from django.contrib.auth.decorators import login_required

def access_denied(request):
    return render(request, 'extra/access_denied.html')


def contact(request):
    """
        İletişim sayfasını çalıştırır.
        Eğer form gönderilmeye uygun ise
        yöneticilere mail atar.
    """
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()        
    
    return render(request, 'extra/contact.html', locals())


@login_required
def became_an_author(request):
    """
        Yazar olma istek formu.
    """
    
    if request.method == 'POST':
        form = AuthorForm(request.POST)
    else:
        form = AuthorForm()
        
    return render(request, 'extra/became_an_author.html', locals())
    
    