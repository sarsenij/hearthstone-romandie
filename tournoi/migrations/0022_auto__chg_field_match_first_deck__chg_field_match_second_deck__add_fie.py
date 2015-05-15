# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Match.first_deck'
        db.alter_column(u'tournoi_match', 'first_deck', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Match.second_deck'
        db.alter_column(u'tournoi_match', 'second_deck', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))
        # Adding field 'Inscrit.confirm'
        db.add_column(u'tournoi_inscrit', 'confirm',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Tournoi.confirmation'
        db.add_column(u'tournoi_tournoi', 'confirmation',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Match.first_deck'
        db.alter_column(u'tournoi_match', 'first_deck', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Match.second_deck'
        db.alter_column(u'tournoi_match', 'second_deck', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Deleting field 'Inscrit.confirm'
        db.delete_column(u'tournoi_inscrit', 'confirm')

        # Deleting field 'Tournoi.confirmation'
        db.delete_column(u'tournoi_tournoi', 'confirmation')


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
        u'tournoi.duel': {
            'Meta': {'object_name': 'Duel'},
            'first': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'first_duel'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'first_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'second': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'second_duel'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'second_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'valide': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'tournoi.inscrit': {
            'Meta': {'object_name': 'Inscrit'},
            'confirm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tournoi': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tournoi_inscrit'", 'to': u"orm['tournoi.Tournoi']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tournoi.invit': {
            'Meta': {'object_name': 'Invit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'tournoi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Tournoi']"})
        },
        u'tournoi.match': {
            'Meta': {'object_name': 'Match'},
            'col': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'conquest_check': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'first_match'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'first_deck': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'freewin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loser_bracket': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'next_gagnant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Match_next_gagnant'", 'null': 'True', 'to': u"orm['tournoi.Match']"}),
            'next_perdant': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Match_next_perdant'", 'null': 'True', 'to': u"orm['tournoi.Match']"}),
            'poule': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'row': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'score_first': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'score_second': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'second_match'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'second_deck': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tournoi': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tournoi_match'", 'null': 'True', 'to': u"orm['tournoi.Tournoi']"}),
            'valide': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'tournoi.tournoi': {
            'Meta': {'object_name': 'Tournoi'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tournoi_admin'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'confirmation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conquest': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'descr': ('django.db.models.fields.TextField', [], {}),
            'finale': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'heure': ('django.db.models.fields.TimeField', [], {'default': "'00:00'", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscrit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'loser_bracket': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'max_participants': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'poules': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'termine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vainqueur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tournoi_vainqueur'", 'null': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['tournoi']