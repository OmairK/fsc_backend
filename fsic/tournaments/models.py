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
    agegroup = models.IntegerField() # +35 +40 +45 +50 +55 +60 +65 +70 +75
    category = models.CharField(max_length=10) # Singles - S; Doubles -D

    class Meta:
        ordering = ['-rank']
    
    def __str__(self):
        return self.name
    


class TournamentFSC(models.Model):
    name = models.CharField(max_length=1000)
    age_group = models.CharField(max_length=500)
    venue = models.CharField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=1000)
    location_url = models.URLField(max_length=300,blank = True) # Google maps link
    coordinator_contact = models.IntegerField(null=True) # Contact No of the event coordinator
    coordinator_email = models.EmailField(max_length=254,null=True)
    coordinator_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
    
    def takes_place_in_future(self):
        return self.date > timezone.now() 

    
