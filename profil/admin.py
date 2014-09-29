# -*- coding: utf-8
from django.contrib import admin

from profil.models import Profil

class ProfilAdmin(admin.ModelAdmin):
    list_display = ['pseudo', 'cote']

admin.site.register(Profil, ProfilAdmin)
