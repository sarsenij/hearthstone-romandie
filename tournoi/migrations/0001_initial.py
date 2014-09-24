# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tournoi'
        db.create_table(u'tournoi_tournoi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('descr', self.gf('django.db.models.fields.TextField')()),
            ('regles', self.gf('django.db.models.fields.TextField')()),
            ('prive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('debut', self.gf('django.db.models.fields.DateTimeField')()),
            ('max_participants', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('match', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('poules', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('loser_bracket', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('finale', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('termine', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'tournoi', ['Tournoi'])

        # Adding model 'Invit'
        db.create_table(u'tournoi_invit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournoi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournoi.Tournoi'])),
            ('invite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'tournoi', ['Invit'])


    def backwards(self, orm):
        # Deleting model 'Tournoi'
        db.delete_table(u'tournoi_tournoi')

        # Deleting model 'Invit'
        db.delete_table(u'tournoi_invit')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tournoi.invit': {
            'Meta': {'object_name': 'Invit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'tournoi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Tournoi']"})
        },
        u'tournoi.tournoi': {
            'Meta': {'object_name': 'Tournoi'},
            'debut': ('django.db.models.fields.DateTimeField', [], {}),
            'descr': ('django.db.models.fields.TextField', [], {}),
            'finale': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loser_bracket': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'max_participants': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'poules': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regles': ('django.db.models.fields.TextField', [], {}),
            'termine': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['tournoi']