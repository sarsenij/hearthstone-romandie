# -*- encoding:utf-8 -*-
from datetime import date,datetime
from time import time
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Tournoi(models.Model):
    name = models.CharField(max_length=225,verbose_name="Nom du tournoi")
    descr = models.TextField(verbose_name="Description et règles")
    prive = models.BooleanField(verbose_name="Tournoi sur invitation",default=False)
    date = models.DateField(verbose_name="Date du tournoi",default=date.today)
    heure = models.TimeField(verbose_name="Heure du tournoi",null=True,default="00:00")
    choices_part = (
    (4,"4"),
    (8,"8"),
    (16,"16"),
    (32,"32"),
    )
    max_participants = models.IntegerField(verbose_name="Participants maximum",choices=choices_part,default=0)
    choices_close = (
    (0,"Non"),
    (1,"BO1"),
    (2,"BO3"),
    (3,"BO5"),
    (4,"BO7"),
    )
    choices_open = (
    (1,"BO1"),
    (2,"BO3"),
    (3,"BO5"),
    (4,"BO7"),
    )
    match = models.IntegerField(verbose_name="Format des matchs",choices=choices_open,default=3)
    finale = models.IntegerField(verbose_name="Format de la finale",choices=choices_open,default=3)
    poules = models.IntegerField(verbose_name="Format des poules",choices=choices_close,default=0)
    loser_bracket = models.IntegerField(verbose_name="Format du loser bracket",choices=choices_close,default=0)
    termine = models.BooleanField(default=False)
    admin = models.ForeignKey('auth.User',null=True,related_name="tournoi_admin")
    inscrit = models.IntegerField(default=0)
    vainqueur = models.ForeignKey('auth.User',null=True,related_name="tournoi_vainqueur",blank=True)

class Invit(models.Model):
    tournoi = models.ForeignKey('Tournoi')
    invite = models.ForeignKey('auth.User')

class Staff(models.Model):
    tournoi = models.ForeignKey('Tournoi')
    admin = models.ForeignKey('auth.User')

class TournoiForm(ModelForm):
    class Meta:
        model = Tournoi
        fields = ['name','descr','prive','date','heure','max_participants','match','finale']#,'poules','loser_bracket']

class Inscrit(models.Model):
    tournoi = models.ForeignKey('Tournoi',related_name="tournoi_inscrit")
    user = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=datetime.now)
    order = models.IntegerField(default=0)

class Match(models.Model):
    tournoi = models.ForeignKey('Tournoi',related_name="tournoi_match",null=True,blank=True)
    first = models.ForeignKey('auth.User',related_name="first_match",null=True,blank=True)
    second = models.ForeignKey('auth.User',related_name="second_match",null=True,blank=True)
    score = models.CharField(null=True,blank=True,max_length=2)
    score_first = models.CharField(null=True,blank=True,max_length=2)
    score_second = models.CharField(null=True,blank=True,max_length=2)
    freewin = models.BooleanField(default=False)
    next_gagnant = models.ForeignKey('Match',null=True,related_name="Match_next_gagnant",blank=True)
    next_perdant = models.ForeignKey('Match',null=True,related_name="Match_next_perdant",blank=True)
    col = models.IntegerField(default=0)
    row = models.IntegerField(default=0)
    valide = models.BooleanField(default=False)

class Duel(models.Model):
    first = models.ForeignKey('auth.User',related_name="first_duel",null=True,blank=True)
    second = models.ForeignKey('auth.User',related_name="second_duel",null=True,blank=True)
    first_score = models.IntegerField(default=0)
    second_score = models.IntegerField(default=0)
    valide = models.BooleanField(default=False)
