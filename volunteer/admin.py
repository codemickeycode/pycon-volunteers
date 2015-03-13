from django.contrib import admin
from .models import Volunteer, Committee, CommitteeChair

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Committee)
admin.site.register(CommitteeChair)