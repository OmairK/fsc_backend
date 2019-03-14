from django.db import models
# Create your models here.

class TournamentITF(models.Model):
    name = models.CharField(max_length = 100)
    venue = models.CharField(max_length = 100)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    surface = models.CharField(max_length = 100)
    grade = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100)
    website = models.CharField(max_length = 100)


class PlayerRankingsMS(models.Model):  #Male Singles
    name = models.CharField(max_length = 50)
    rank = models.IntegerField()
    movement = models.IntegerField()
    dob = models.IntegerField()
    events = models.IntegerField()
    points = models.IntegerField()

class PlayerRankingsMD(models.Model):   #Male Doubles
    name = models.CharField(max_length = 50)
    rank = models.IntegerField()
    movement = models.IntegerField()
    dob = models.IntegerField()
    events = models.IntegerField()
    points = models.IntegerField()



class TournamentFSC(models.Model):
    name = models.CharField(max_length = 1000)
    age_group = models.CharField(max_length = 500)
    venue = models.CharField(max_length = 1000)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length = 1000)

