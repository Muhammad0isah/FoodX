from django.contrib import admin
from .models import ISADMembers


# Register your models here

class ISADMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment','image')

admin.site.register(ISADMembers, ISADMemberAdmin)
