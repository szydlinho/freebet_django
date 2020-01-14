from django.db import models

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



class Matches_Pred_Upcoming(models.Model):
    date = models.DateField()
    league = models.CharField(max_length=5)
    MW = models.IntegerField(default = 0)
    HomeTeam = models.CharField(max_length=200)
    AwayTeam = models.CharField(max_length=200)
    model = models.CharField(max_length=5)
    prediction = models.CharField(max_length=5)
    proba = models.FloatField(default=0)
