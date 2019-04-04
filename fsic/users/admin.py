from django.contrib import admin
from .models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):
    fields = ['name','date_of_birth','cien_no']

admin.site.register(UserProfile, UserProfileAdmin)
