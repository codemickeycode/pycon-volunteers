from django.contrib import admin
from .models import Volunteer, Committee, CommitteeChair

# Register your models here.
class CommiteeAdmin(admin.ModelAdmin):
    list_display = ('committee_id', 'name', 'slots_available', 'slots_taken')

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'email', 'contactno',
        'message', 'created_date',
        'committee_id', 'related_committee')
    def related_committee(self, obj):
        return '%s'%(obj.committee_id.name)
    related_committee.short_description = 'Committee Name'

class CommitteeChairAdmin(admin.ModelAdmin):
    list_display = ('name', 'committee_id', 'related_committee')
    def related_committee(self, obj):
        return '%s'%(obj.committee_id.name)
    related_committee.short_description = 'Committee Name'

admin.site.register(Committee, CommiteeAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(CommitteeChair, CommitteeChairAdmin)
