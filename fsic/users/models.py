from django.db import models
from django.core import validators
from django.contrib.auth.models import User

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
    achievements = models.CharField(
        max_length=250,
        null=True,
        )
    city = models.CharField(
        max_length=100,
        null=True,
        )
    name = models.CharField(max_length=100)
    home_club = models.CharField(
        max_length=100,
        )
    date_of_birth = models.DateField( 
        auto_now=False, 
        auto_now_add=False,
        )
    # contact_no = models.BigIntegerField(null=True)
    profession = models.CharField( 
        max_length=100,
        )
    user_email = models.EmailField( 
        max_length=254,
        )
    role_model = models.CharField(
        max_length=100,
        )   
    cien_no = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        )
    player_id = models.AutoField(primary_key=True)
    profile_photo = models.URLField(
        max_length=200,
        null=True)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name



