# -*- encoding:utf-8 -*-
from datetime import date,datetime
from time import time
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Tournoi(models.Model):
    name = models.CharField(max_length=225,verbose_name="Nom du tournoi")
    descr = models.TextField(verbose_name="Description")
    regles = models.TextField(verbose_name="Règles spécifiques")
    prive = models.BooleanField(verbose_name="Tournoi sur invitation",default=False)
    date = models.DateField(verbose_name="Date du tournoi",default=date.today)
    heure = models.TimeField(verbose_name="Heure du tournoi",null=True,default="00:00:00")
    choices_part = (
    (4,"4"),
    (8,"8"),
    (16,"16"),
    (32,"32"),
    (64,"64"),
    )
    max_participants = models.IntegerField(verbose_name="Participants maximum",choices=choices_part,default=0)
    choices_close = (
    (0,"Non"),
    (1,"BO1"),
    (3,"BO3"),
    (5,"BO5"),
    (7,"BO7"),
    )
    choices_open = (
    (1,"BO1"),
    (3,"BO3"),
    (5,"BO5"),
    (7,"BO7"),
    )
    match = models.IntegerField(verbose_name="Format des matchs",choices=choices_open,default=3)
    poules = models.IntegerField(verbose_name="Format des poules",choices=choices_close,default=0)
    loser_bracket = models.IntegerField(verbose_name="Format du loser bracket",choices=choices_close,default=0)
    finale = models.IntegerField(verbose_name="Format de la finale",choices=choices_open,default=3)
    termine = models.BooleanField(default=False)
    admin = models.ForeignKey('auth.User',null=True,related_name="tournoi_admin")
    inscrit = models.IntegerField(default=0)
    vainqueur = models.ForeignKey('auth.User',null=True,related_name="tournoi_vainqueur")

class Invit(models.Model):
    tournoi = models.ForeignKey('Tournoi')
    invite = models.ForeignKey('auth.User')

class Staff(models.Model):
    tournoi = models.ForeignKey('Tournoi')
    admin = models.ForeignKey('auth.User')

class TournoiForm(ModelForm):
    class Meta:
        model = Tournoi
        fields = ['name','descr','regles','prive','date','heure','max_participants','match','finale','poules','loser_bracket']

class Inscrit(models.Model):
    tournoi = models.ForeignKey('Tournoi',related_name="tournoi_inscrit")
    user = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=datetime.now)
    order = models.IntegerField(default=0)

class Match(models.Model):
    first = models.ForeignKey('auth.User',related_name="first_match",null=True)
    second = models.ForeignKey('auth.User',related_name="second_match",null=True)
    score_first = models.IntegerField(default=0)
    score_second = models.IntegerField(default=0)
    score_first_by_first = models.IntegerField(default=0)
    score_second_by_first = models.IntegerField(default=0)
    score_first_by_second = models.IntegerField(default=0)
    score_second_by_second = models.IntegerField(default=0)
    first_freewin = models.BooleanField(default=False)
    second_freewin = models.BooleanField(default=False)

class Arbre(models.Model):
    tournoi = models.ForeignKey('Tournoi')
    finale_loser = models.ForeignKey('Match',related_name="finale_loser",null=True)
    finale = models.ForeignKey('Match',related_name="finale",null=True)
    petitefinale = models.ForeignKey('Match',related_name="petitefinale",null=True)
    demifinale = models.ForeignKey('DemiFinale',null=True)
    quart = models.ForeignKey('Quart',null=True)
    huitieme = models.ForeignKey('Huitieme',null=True)
    seizieme = models.ForeignKey('Seizieme',null=True)
    trentedeuxieme = models.ForeignKey('Trentedeuxieme',null=True)
    poule1 = models.ForeignKey('Poule',null=True,related_name="poule1")
    poule2 = models.ForeignKey('Poule',null=True,related_name="poule2")
    poule3 = models.ForeignKey('Poule',null=True,related_name="poule3")
    poule4 = models.ForeignKey('Poule',null=True,related_name="poule4")
    poule5 = models.ForeignKey('Poule',null=True,related_name="poule5")
    poule6 = models.ForeignKey('Poule',null=True,related_name="poule6")
    poule7 = models.ForeignKey('Poule',null=True,related_name="poule7")
    poule8 = models.ForeignKey('Poule',null=True,related_name="poule8")
    poule9 = models.ForeignKey('Poule',null=True,related_name="poule9")
    poule10 = models.ForeignKey('Poule',null=True,related_name="poule10")
    poule11 = models.ForeignKey('Poule',null=True,related_name="poule11")
    poule12 = models.ForeignKey('Poule',null=True,related_name="poule12")
    poule13 = models.ForeignKey('Poule',null=True,related_name="poule13")
    poule14 = models.ForeignKey('Poule',null=True,related_name="poule14")
    poule15 = models.ForeignKey('Poule',null=True,related_name="poule15")
    poule16 = models.ForeignKey('Poule',null=True,related_name="poule16")

class DemiFinale(models.Model):
    match1 = models.ForeignKey('Match',related_name="demifinale_match1")
    match2 = models.ForeignKey('Match',related_name="demifinale_match2")

class Quart(models.Model):
    match1 = models.ForeignKey('Match',related_name="quart_match1")
    match2 = models.ForeignKey('Match',related_name="quart_match2")
    match3 = models.ForeignKey('Match',related_name="quart_match3")
    match4 = models.ForeignKey('Match',related_name="quart_match4")

class Huitieme(models.Model):
    match1 = models.ForeignKey('Match',related_name="huitieme_match1")
    match2 = models.ForeignKey('Match',related_name="huitieme_match2")
    match3 = models.ForeignKey('Match',related_name="huitieme_match3")
    match4 = models.ForeignKey('Match',related_name="huitieme_match4")
    match5 = models.ForeignKey('Match',related_name="huitieme_match5")
    match6 = models.ForeignKey('Match',related_name="huitieme_match6")
    match7 = models.ForeignKey('Match',related_name="huitieme_match7")
    match8 = models.ForeignKey('Match',related_name="huitieme_match8")

class Seizieme(models.Model):
    match1 = models.ForeignKey('Match',related_name="seizieme_match1")
    match2 = models.ForeignKey('Match',related_name="seizieme_match2")
    match3 = models.ForeignKey('Match',related_name="seizieme_match3")
    match4 = models.ForeignKey('Match',related_name="seizieme_match4")
    match5 = models.ForeignKey('Match',related_name="seizieme_match5")
    match6 = models.ForeignKey('Match',related_name="seizieme_match6")
    match7 = models.ForeignKey('Match',related_name="seizieme_match7")
    match8 = models.ForeignKey('Match',related_name="seizieme_match8")
    match9 = models.ForeignKey('Match',related_name="seizieme_match9")
    match10 = models.ForeignKey('Match',related_name="seizieme_match10")
    match11 = models.ForeignKey('Match',related_name="seizieme_match11")
    match12 = models.ForeignKey('Match',related_name="seizieme_match12")
    match13 = models.ForeignKey('Match',related_name="seizieme_match13")
    match14 = models.ForeignKey('Match',related_name="seizieme_match14")
    match15 = models.ForeignKey('Match',related_name="seizieme_match15")
    match16 = models.ForeignKey('Match',related_name="seizieme_match16")

class Trentedeuxieme(models.Model):
    match1 = models.ForeignKey('Match',related_name="trentedeuxieme_match1")
    match2 = models.ForeignKey('Match',related_name="trentedeuxieme_match2")
    match3 = models.ForeignKey('Match',related_name="trentedeuxieme_match3")
    match4 = models.ForeignKey('Match',related_name="trentedeuxieme_match4")
    match5 = models.ForeignKey('Match',related_name="trentedeuxieme_match5")
    match6 = models.ForeignKey('Match',related_name="trentedeuxieme_match6")
    match7 = models.ForeignKey('Match',related_name="trentedeuxieme_match7")
    match8 = models.ForeignKey('Match',related_name="trentedeuxieme_match8")
    match9 = models.ForeignKey('Match',related_name="trentedeuxieme_match9")
    match10 = models.ForeignKey('Match',related_name="trentedeuxieme_match10")
    match11 = models.ForeignKey('Match',related_name="trentedeuxieme_match11")
    match12 = models.ForeignKey('Match',related_name="trentedeuxieme_match12")
    match13 = models.ForeignKey('Match',related_name="trentedeuxieme_match13")
    match14 = models.ForeignKey('Match',related_name="trentedeuxieme_match14")
    match15 = models.ForeignKey('Match',related_name="trentedeuxieme_match15")
    match16 = models.ForeignKey('Match',related_name="trentedeuxieme_match16")
    match17 = models.ForeignKey('Match',related_name="trentedeuxieme_match17")
    match18 = models.ForeignKey('Match',related_name="trentedeuxieme_match18")
    match19 = models.ForeignKey('Match',related_name="trentedeuxieme_match19")
    match20 = models.ForeignKey('Match',related_name="trentedeuxieme_match20")
    match21 = models.ForeignKey('Match',related_name="trentedeuxieme_match21")
    match22 = models.ForeignKey('Match',related_name="trentedeuxieme_match22")
    match23 = models.ForeignKey('Match',related_name="trentedeuxieme_match23")
    match24 = models.ForeignKey('Match',related_name="trentedeuxieme_match24")
    match25 = models.ForeignKey('Match',related_name="trentedeuxieme_match25")
    match26 = models.ForeignKey('Match',related_name="trentedeuxieme_match26")
    match27 = models.ForeignKey('Match',related_name="trentedeuxieme_match27")
    match28 = models.ForeignKey('Match',related_name="trentedeuxieme_match28")
    match29 = models.ForeignKey('Match',related_name="trentedeuxieme_match29")
    match30 = models.ForeignKey('Match',related_name="trentedeuxieme_match30")
    match31 = models.ForeignKey('Match',related_name="trentedeuxieme_match31")
    match32 = models.ForeignKey('Match',related_name="trentedeuxieme_match32")

class Poule(models.Model):
    match1 = models.ForeignKey('Match',related_name="poule_match1")
    match2 = models.ForeignKey('Match',related_name="poule_match2")
    match3 = models.ForeignKey('Match',related_name="poule_match3")
    match4 = models.ForeignKey('Match',related_name="poule_match4")
    match5 = models.ForeignKey('Match',related_name="poule_match5")
    match6 = models.ForeignKey('Match',related_name="poule_match6")
