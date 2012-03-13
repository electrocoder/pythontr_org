# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from pythontr_org.extra.forms import ContactForm

def access_denied(request):
    return render(request, 'extra/access_denied.html')


def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()        
    
    return render(request, 'extra/contact.html', locals())