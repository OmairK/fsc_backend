from django.db import models
from django.core.validators import (
            EmailValidator,URLValidator)
from django.core import validators
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 2*1024*1024:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value
class UserProfile(models.Model):
    Dominant_Hand = (
        ('RIGHT' , 'Right'),
        ('LEFT' , 'Left'),
    )
    Backhand_Play_Styles = (
        ('SINGLE','Single'),
        ('DOUBLE' , 'Double'),
        ('BOTH' , 'Both'),
    )
    name = models.CharField(max_length=100)
    user_email = models.EmailField(
        validators=[EmailValidator],
        blank = True, 
        max_length=254,
        )
    strong_hand = models.CharField(
        max_length=15,
        choices=Dominant_Hand,
        default='RIGHT',
        )
    backhand_style = models.CharField(
        max_length=20,
        choices=Backhand_Play_Styles,
        default='SINGLE',
        )
    achievements = models.TextField(
        blank = True,
        max_length=500,
        null=True,
        default = "Dedicated senior tennis player",
        )
    city = models.CharField(
        blank = True,
        max_length=100,
        null=True,
        )
    
    home_club = models.CharField(
        blank = True,
        max_length=100,
        )
    date_of_birth = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        )
    profession = models.CharField(
        blank = True, 
        max_length=100,
        )
    
    role_model = models.CharField(
        blank = True,
        max_length=100,
        )   
    cien_no = models.CharField(
        blank = True,
        max_length=10,
        unique=True,
        null=True,
        )
    player_id = models.AutoField(primary_key=True)
    profile_photo = models.ImageField(
	    upload_to='images/',
        blank = True,
        max_length=1000,
        null=True,
        validators=[validate_file_size],)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name



