from django.db import models
from django.core.validators import (
            MaxValueValidator,MinValueValidator,
            EmailValidator,URLValidator)
from django.core.exceptions import ValidationError

class TournamentITF(models.Model):
    tournament_name = models.CharField(max_length=100)
    host_nation = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    venue = models.CharField(max_length=100)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    surface = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    website = models.CharField(
        max_length=100,
        blank=True,
        null=True)

    def __str__(self):
        return self.name


class PlayerRankingsMS(models.Model):  # Male Singles/Doubles
    name = models.CharField(max_length=150)
    rank = models.IntegerField()
    movement = models.IntegerField()
    dob = models.IntegerField()
    events = models.IntegerField()
    points = models.FloatField()
    age_group = models.CharField(max_length = 5) # +35 +40 +45 +50 +55 +60 +65 +70 +75
    category = models.CharField(max_length=10) # Singles - S; Doubles -D

    class Meta:
        ordering = ['rank']
    
    def __str__(self):
        return self.name
    


class TournamentFSC(models.Model):
    tournament_name = models.CharField(max_length=1000)
    age_group = models.CharField(max_length=100)
    tournament_venue = models.CharField(max_length=1000)
    date = models.DateField(
        auto_now=False, 
        auto_now_add=False)
    tournament_description = models.CharField(max_length=1000)
    event_location_url = models.URLField(       # Google maps link
        validators=[URLValidator],
        max_length=300,
        blank = True,
        null=True) 
    coordinator_name = models.CharField(
        max_length=100,
        null=True)
    coordinator_contact_number = models.BigIntegerField(
        validators=[
            MaxValueValidator(10000000000,message="Enter a valid phone number"),
            MinValueValidator(1000000000,message="Enter a valid phone number")],
        null=True) # Contact No of the event coordinator
    coordinator_email = models.EmailField(
        validators=[EmailValidator],
        max_length=254,
        null=True)
    

    def __str__(self):
        return self.tournament_name
    
    def takes_place_in_future(self):
        return self.date > timezone.now() 

    
