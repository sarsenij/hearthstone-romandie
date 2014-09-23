# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, default=datetime.now)
    position = models.IntegerField(blank=True, default=0, db_index=True)
    staff = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Forum(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, default=datetime.now)
    category = models.ForeignKey('pybb.Category', related_name='forums')
    position = models.IntegerField(blank=True, default=0, db_index=True)
    topic_count = models.IntegerField(blank=True, default=0)
    post_count = models.IntegerField(blank=True, default=0)
    staff = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pybb:forum_page', args=[self.pk])


class Topic(models.Model):
    name = models.CharField(u'Nom du topic', max_length=100)
    created = models.DateTimeField(blank=True, default=datetime.now)
    edit = models.DateTimeField(blank=True, default=datetime.now)
    forum = models.ForeignKey('pybb.Forum', related_name='topics')
    post_count = models.IntegerField(blank=True, default=0)
    postit = models.BooleanField(default=False)
    close = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pybb:topic_page', args=[self.pk])
    class Meta:
        ordering = ['-edit']


class Post(models.Model):
    created = models.DateTimeField(blank=True, default=datetime.now)
    topic = models.ForeignKey('pybb.Topic', related_name='posts')
    content = models.TextField(u'Соntenu')
    content_html = models.TextField(blank=True)
    user = models.ForeignKey('auth.User',related_name='post_author')
    modif_user = models.ForeignKey('auth.User',related_name='post_modif',null=True,blank=True)
    modif_date = models.DateTimeField(blank=True, default=datetime.now)
    locked = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey('auth.User',related_name='post_deleted',null=True,blank=True)

    def __unicode__(self):
        return self.topic.name


import pybb.signals

class Dejavu(models.Model) :
    compte = models.ForeignKey('auth.User')
    forum = models.ForeignKey('pybb.Forum')
    topic = models.ForeignKey('pybb.Topic')
    post = models.IntegerField(default=0)

class Suivi(models.Model) :
    user = models.ForeignKey('auth.User')
    topic = models.ForeignKey('pybb.Topic')
