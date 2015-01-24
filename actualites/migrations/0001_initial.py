# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Horaire'
        db.create_table(u'actualites_horaire', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'actualites', ['Horaire'])


    def backwards(self, orm):
        # Deleting model 'Horaire'
        db.delete_table(u'actualites_horaire')


    models = {
        u'actualites.horaire': {
            'Meta': {'object_name': 'Horaire'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['actualites']