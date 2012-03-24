# -*- coding: utf-8-*-

from pythontr_org.polls.models import Poll, Choice, Vote
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question', 'slug']}),
    ]
    inlines = [ChoiceInline]
    
    prepopulated_fields = {'slug': ('question', )}


class VoteAdmin(admin.ModelAdmin):
    actions = ['really_delete_selected']
    
    def get_actions(self, request):
        actions = super(VoteAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        self.message_user(request, u"%s oy başarı ile silindi." % queryset.count())
    really_delete_selected.short_description = u"Seçili oyları sil"
    
    
    list_display = ('user', 'poll', 'choice', 'created_at')


admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)