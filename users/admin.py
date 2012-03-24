# -*- coding: utf-8 -*-

from django.contrib import admin
from pythontr_org.users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['web_site', 'about', 'city']    
    list_display = ('user', 'web_site', 'city')


admin.site.register(Profile, ProfileAdmin)