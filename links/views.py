# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from pythontr_org.links.models import Link


def index(request):    
    links = Link.objects.all()
    
    return render(request, 'links/index.html', locals())