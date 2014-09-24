from django.db import models
from datetime import datetime
from profil.models import Profil, Contact
from tournoi.models import Tournoi

# Create your models here.

class Notification(models.Model) :
    destinataire = models.ForeignKey(Profil)
    contact = models.ForeignKey(Contact,null=True,blank=True)
    contact_already = models.BooleanField(default=False)
    vue = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)

class Titre(models.Model):
    titre = models.CharField(max_length=100)
    edit = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-edit']

class Dest(models.Model):
    titre = models.ForeignKey('Titre')
    dest = models.ForeignKey('auth.User')

class Message(models.Model):
    created = models.DateTimeField(default=datetime.now)
    titre = models.ForeignKey('Titre')
    content = models.TextField()
    user = models.ForeignKey('auth.User')

class Dejavu(models.Model) :
    compte = models.ForeignKey('auth.User',related_name='message_dejavu')
    titre = models.ForeignKey('Titre')
    message = models.ForeignKey('Message')

class ChatMsg(models.Model) :
    user = models.ForeignKey('auth.User')
    message = models.TextField()
    created = models.DateTimeField(default=datetime.now)

class InviteTournoi(models.Model) :
    user = models.ForeignKey('auth.User')
    tournoi = models.ForeignKey('tournoi.Tournoi')
    staff = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
