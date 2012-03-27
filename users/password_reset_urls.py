# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url


PASSWORD_RESET_DICT = {
                       'post_reset_redirect': '/accounts/password_reset/done/',
                       'email_template_name': 'users/mails/password_reset.html',
                       'template_name': 'users/password_reset.html'
}

PASSWORD_RESET_CONFIRM_DICT = {
                               'post_reset_redirect': '/accounts/password_reset/complete/',
                               'template_name': 'users/password_reset_confirm.html',
}

urlpatterns = patterns('django.contrib.auth.views',
                        url(r'^$', 'password_reset', PASSWORD_RESET_DICT),
                        url(r'^complete/$', 'password_reset_complete', {'template_name': 'users/password_reset_complete.html'}),
                        url(r'^confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', PASSWORD_RESET_CONFIRM_DICT),
                        url(r'^done/$', 'password_reset_done', {'template_name': 'users/password_reset_done.html'}),

)