from django.db import models
# Create your models here.

class TournamentITF(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    venue = models.CharField(max_length = 100)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    surface = models.CharField(max_length = 30)
    grade = models.CharField(max_length = 10)
    link = models.CharField(max_length = 100)


class PlayerRankingsMS(models.Model):  #Male Singles
    name = models.CharField(max_length = 50)
    rank = models.IntegerField()

class PlayerRankingsMD(models.Model):   #Male Doubles
    name = models.CharField(max_length = 50)
    rank = models.IntegerField()

class PlayerRankingsFS(models.Model):   #Female Singles
    name = models.CharField(max_length = 50)
    rank = models.IntegerField()

class PlayerRankingsFD(models.Model):   #Female Doubles
    name = models.CharField(max_length = 50)
    rank = models.IntegerField()

class TournamentFSC(models.Model):
    name = models.CharField(max_length = 100)
    age_group = models.CharField(max_length = 50)
    venue = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)

