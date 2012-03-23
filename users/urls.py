# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout, password_change
from django.contrib.auth.views import password_reset, password_reset_complete, password_reset_confirm, password_reset_done


PASSWORD_CHANGE_DICT = {
                   'template_name': 'users/password_change.html',
                   'post_change_redirect': '/accounts/settings/'
}


urlpatterns = patterns('pythontr_org.users.views',
                       # yazarlar
                       url(r'^authors/$', 'authors', name = 'authors'),
                       
                       # Giriş ve çıkış
                       url(r'^login/$', login, {'template_name': 'users/login.html'}, name = 'login'),
                       url(r'^logout/$', logout, { 'next_page': '/py/' }, name = 'logout'),
                       
                       # kayıt olma ve şifre değiştirme
                       url(r'^signup/$', 'signup', name = 'signup'),
                       url(r'^password_change/$', password_change, PASSWORD_CHANGE_DICT, name = 'password_change'),
                                           
                       # hesabı dondurma
                       url(r'^disable/$', 'disable', name = 'disable_account'),
                       
                       # profil gösterme
                       url(r'^profile/(?P<username>[^/]*)/', 'show', name = 'show_profile'),
                       
                       # profil ve hesap ayarları
                       url(r'^settings/$', 'settings', name = 'settings'),                       
                       url(r'^settings/update_informations/$', 'update_informations', name = 'update_informations'),
                       url(r'^settings/update_profile/$', 'update_profile', name = 'update_profile'),                      
)

# Parola sıfırlama ile ilgili

PASSWORD_RESET_DICT = {
                       'post_reset_redirect': '/accounts/password_reset/done/',
                       'email_template_name': 'emails/password_reset.html',
                       'template_name': 'users/password_reset.html'
}

PASSWORD_RESET_CONFIRM_DICT = {
                               'post_reset_redirect': '/accounts/password_reset/complete/',
                               'template_name': 'users/password_reset_confirm.html',
}

urlpatterns += patterns('django.contrib.auth.views',
                        url(r'^password_reset/$', 'password_reset', PASSWORD_RESET_DICT),
                        url(r'^password_reset/complete/$', 'password_reset_complete', {'template_name': 'users/password_reset_complete.html'}),
                        url(r'^password_reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', PASSWORD_RESET_CONFIRM_DICT),
                        url(r'^password_reset/done/$', 'password_reset_done', {'template_name': 'users/password_reset_done.html'}),

)