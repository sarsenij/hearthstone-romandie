from datetime import datetime

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Pays(models.Model) :
    pays = models.CharField(max_length=125)

class VilleProche(models.Model) :
    
    ville_proche = models.CharField(max_length=125)

class Localite(models.Model) :
    
    localite = models.CharField(max_length=125)

class Profil(models.Model) :
    
    PRIVACY_CHOICES = (
    (0,"Moi"),
    (1,"Mes contacts"),
    (2,"Public"),
    )

    u = models.ForeignKey(User)

    pseudo = models.CharField(max_length=125)

    avatar = models.CharField(max_length=250,blank=True,null=True,default="/static/images/avatars/avatar.png")

    nom = models.CharField(max_length=125,blank=True,null=True,default="")
    nom_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=0)

    prenom = models.CharField(max_length=125,blank=True,null=True,default="")
    prenom_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=0)

    email = models.CharField(max_length=125,null=True,blank=True,default="")
    email_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=0)
    
    rue = models.CharField(max_length=125,blank=True,null=True,default="")
    rue_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=0)

    localite = models.ForeignKey(Localite,blank=True,null=True,default=1)
    localite_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=2)

    ville_proche = models.ForeignKey(VilleProche,blank=True,null=True,default=1)
    ville_proche_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=2)

    pays = models.ForeignKey(Pays,blank=True,null=True,default=1)
    pays_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=2)

    battletag = models.CharField(max_length=125,blank=True,null=True,default="")
    battletag_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=0)

    telephone = models.CharField(max_length=125,blank=True,null=True,default="")
    telephone_privacy = models.IntegerField(choices=PRIVACY_CHOICES,default=0)

    lastseen = models.DateTimeField(null=True,default=datetime.now)

    cote = models.IntegerField(default=1000)

class Contact(models.Model) :

    owner = models.ForeignKey(Profil, related_name="owner")
    contact = models.ForeignKey(Profil, related_name="contact")
