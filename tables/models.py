from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Matches_Pred(models.Model):
    date = models.DateField()
    league = models.CharField(max_length=5)
    MW =   models.IntegerField(default = 0)
    HomeTeam = models.CharField(max_length=200)
    AwayTeam =  models.CharField(max_length=200)
    model = models.CharField(max_length=5)
    prediction = models.CharField(max_length=5)
    Result = models.CharField(max_length=10)
    result_binary =  models.IntegerField()
    corrected =  models.IntegerField()
    proba = models.FloatField(default=0)

    def __str__(self):
        return "{} {} {} {} {} {}".format( self.date,self.league, self.model, self.HomeTeam, self.AwayTeam,  self.prediction)

    def save(self, *args, **kwargs):
        self.abb = slugify(self.league)
        super().save(*args, **kwargs)

#    def get_absolute_url(self):
#        return reverse('league_tab',
#                       args=[str(self.abb)])



class Matches_Pred_History(models.Model):
    date = models.DateField()
    league = models.CharField(max_length=5)
    MW =   models.IntegerField(default = 0)
    HomeTeam = models.CharField(max_length=200)
    AwayTeam =  models.CharField(max_length=200)
    model = models.CharField(max_length=5)
    prediction = models.CharField(max_length=5)
    Result = models.CharField(max_length=10)
    result_binary =  models.IntegerField()
    corrected =  models.IntegerField()
    proba = models.FloatField(default=0)

    def __str__(self):
        return "{} {} {} {} {} {}".format( self.date,self.league, self.model, self.HomeTeam, self.AwayTeam,
                                           self.prediction)

    def save(self, *args, **kwargs):
        self.league = slugify(self.league)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/pred/{self.league}'

#    def get_absolute_url(self):
#        return reverse('league_tab',
#                       args=[str(self.abb)])



class Matches_Pred_Upcoming(models.Model):
    date = models.DateField()
    league = models.CharField(max_length=5)
    MW = models.IntegerField(default = 0)
    HomeTeam = models.CharField(max_length=200)
    AwayTeam = models.CharField(max_length=200)
    model = models.CharField(max_length=5)
    prediction = models.CharField(max_length=5)
    proba = models.FloatField(default=0)

    def __str__(self):
        return "{} {} {} {} {} {}".format( self.date,self.league, self.model, self.HomeTeam, self.AwayTeam,  self.prediction)

    def save(self, *args, **kwargs):
        self.abb = slugify(self.league)
        super().save(*args, **kwargs)

#    def get_absolute_url(self):
#        return reverse('league_tab',
#                       args=[str(self.abb)])
