from django.db import models


class TournamentITF(models.Model):
    name = models.CharField(max_length=100)
    host_nation = models.CharField(max_length=100, blank=True, null=True)
    venue = models.CharField(max_length=100)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    surface = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class PlayerRankingsMS(models.Model):  # Male Singles/Doubles
    name = models.CharField(max_length=150)
    rank = models.IntegerField()
    movement = models.IntegerField()
    dob = models.CharField(max_length=50)
    events = models.IntegerField()
    points = models.FloatField()
    agegroup = models.IntegerField()
    category = models.CharField(max_length=10)

    class Meta:
        ordering = ['-rank']
    
    def __str__(self):
        return self.name
    


class TournamentFSC(models.Model):
    name = models.CharField(max_length=1000)
    age_group = models.CharField(max_length=500)
    venue = models.CharField(max_length=1000)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
