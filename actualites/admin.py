# -*- coding: utf-8
from django.contrib import admin

from actualites.models import Horaire

class HoraireAdmin(admin.ModelAdmin):
    list_display = ['content']

admin.site.register(Horaire, HoraireAdmin)
