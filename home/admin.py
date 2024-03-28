from django.contrib import admin
from .models import HeroSection,UserComment

admin.site.register(HeroSection)

class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment','image')
admin.site.register(UserComment, UserCommentAdmin)