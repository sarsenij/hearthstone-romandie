# -*- coding: utf-8
from django.contrib import admin

from tournoi.models import Tournoi, Match, Inscrit

class TournoiAdmin(admin.ModelAdmin):
    list_display = ['name','date']

class MatchAdmin(admin.ModelAdmin):
    list_display = ['tournoi','id','col','row']

class InscritAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Tournoi, TournoiAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Inscrit, InscritAdmin)
