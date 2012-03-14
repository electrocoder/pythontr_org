# -*- coding: utf-8-*-

from pythontr_org.polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)