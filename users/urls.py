# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout, password_change


PASSWORD_CHANGE_DICT = {
                   'template_name': 'users/password_change.html',
                   'post_change_redirect': '/accounts/settings/'
}


urlpatterns = patterns('pythontr_org.users.views',
                       # yazarlar
                       url(r'^authors/$', 'authors', name = 'authors'),
                       
                       # Giriş ve çıkış
                       url(r'^login/$', login, {'template_name': 'users/login.html'}, name = 'login'),
                       url(r'^logout/$', logout, { 'next_page': '/posts/' }, name = 'logout'),
                       
                       # kayıt olma ve şifre değiştirme
                       url(r'^signup/$', 'signup', name = 'signup'),
                       url(r'^password_change/$', password_change, PASSWORD_CHANGE_DICT, name = 'password_change'),
                       
                       # hesabı dondurma
                       url(r'^disable_account/$', 'disable', name = 'disable_account'),
                       
                       # profil gösterme
                       url(r'^profile/(?P<username>[^/]*)/', 'show', name = 'show_profile'),
                       
                       # profil ve hesap ayarları
                       url(r'^settings/$', 'settings', name = 'settings'),                       
                       url(r'^settings/update_informations/$', 'update_informations', name = 'update_informations'),
                       url(r'^settings/update_profile/$', 'update_profile', name = 'update_profile'),                      
)