from django.contrib import admin
from .models import Event



class EventAdmin(admin.ModelAdmin):
    list_display = ('name',)




# Register your models here.
admin.site.register(Event, EventAdmin)
