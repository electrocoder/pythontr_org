# -*- coding: utf-8 -*-

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib import admin
from django import forms


class LargeTextAreaFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=forms.Textarea(
                attrs={'cols': 100, 'rows': 30},
            ))
        return super(LargeTextAreaFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, LargeTextAreaFlatPageAdmin)
