# -*- coding: utf-8-*-
# Projenin Adi : PythonTR-Türk Python' cular...
# Tarih : 2008-2011
# Yazar : pythontr.org ekibi
# Kontak : admin@pythontr.org
# Web : http://pythontr.org
# Python Versiyonu : 2.6-2.7
# Django Versiyonu : 1.2.5
# Amaci : www.pythontr.org sitesinin Django framework ile acik kaynakli kodlanmasi...
#         Eklemek isteginiz kodlar icin irtibat kurunuz...
#
#         http://pythontr.org
#
from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.polls.views',
    (r'^$', 'index'),
    (r'^(?P<poll_id>\d+)/$', 'detail'),
    (r'^(?P<poll_id>\d+)/results/$', 'results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
