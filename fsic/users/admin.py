from django.contrib import admin
from .models import UserProfile
from django.forms import TextInput, Textarea
from django.db import models



class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('name', 'cien_no')
    
    


    

admin.site.register(UserProfile,UserProfileAdmin)
