# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tournoi.vainqueur'
        db.add_column(u'tournoi_tournoi', 'vainqueur',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='tournoi_vainqueur', null=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tournoi.vainqueur'
        db.delete_column(u'tournoi_tournoi', 'vainqueur_id')


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
        u'tournoi.arbre': {
            'Meta': {'object_name': 'Arbre'},
            'demifinale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.DemiFinale']", 'null': 'True'}),
            'finale': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finale'", 'null': 'True', 'to': u"orm['tournoi.Match']"}),
            'finale_loser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finale_loser'", 'null': 'True', 'to': u"orm['tournoi.Match']"}),
            'huitieme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Huitieme']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'petitefinale': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'petitefinale'", 'null': 'True', 'to': u"orm['tournoi.Match']"}),
            'poule1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule1'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule10': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule10'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule11': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule11'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule12': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule12'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule13': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule13'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule14': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule14'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule15': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule15'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule16': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule16'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule2'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule3'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule4'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule5'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule6'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule7': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule7'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule8': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule8'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'poule9': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule9'", 'null': 'True', 'to': u"orm['tournoi.Poule']"}),
            'quart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Quart']", 'null': 'True'}),
            'seizieme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Seizieme']", 'null': 'True'}),
            'tournoi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Tournoi']"}),
            'trentedeuxieme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Trentedeuxieme']", 'null': 'True'})
        },
        u'tournoi.demifinale': {
            'Meta': {'object_name': 'DemiFinale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demifinale_match1'", 'to': u"orm['tournoi.Match']"}),
            'match2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demifinale_match2'", 'to': u"orm['tournoi.Match']"})
        },
        u'tournoi.huitieme': {
            'Meta': {'object_name': 'Huitieme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match1'", 'to': u"orm['tournoi.Match']"}),
            'match2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match2'", 'to': u"orm['tournoi.Match']"}),
            'match3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match3'", 'to': u"orm['tournoi.Match']"}),
            'match4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match4'", 'to': u"orm['tournoi.Match']"}),
            'match5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match5'", 'to': u"orm['tournoi.Match']"}),
            'match6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match6'", 'to': u"orm['tournoi.Match']"}),
            'match7': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match7'", 'to': u"orm['tournoi.Match']"}),
            'match8': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'huitieme_match8'", 'to': u"orm['tournoi.Match']"})
        },
        u'tournoi.inscrit': {
            'Meta': {'object_name': 'Inscrit'},
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
            'first': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'first_match'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'first_freewin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score_first': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_first_by_first': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_first_by_second': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_second': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_second_by_first': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_second_by_second': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'second': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'second_match'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'second_freewin': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'tournoi.poule': {
            'Meta': {'object_name': 'Poule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule_match1'", 'to': u"orm['tournoi.Match']"}),
            'match2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule_match2'", 'to': u"orm['tournoi.Match']"}),
            'match3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule_match3'", 'to': u"orm['tournoi.Match']"}),
            'match4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule_match4'", 'to': u"orm['tournoi.Match']"}),
            'match5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule_match5'", 'to': u"orm['tournoi.Match']"}),
            'match6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poule_match6'", 'to': u"orm['tournoi.Match']"})
        },
        u'tournoi.quart': {
            'Meta': {'object_name': 'Quart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quart_match1'", 'to': u"orm['tournoi.Match']"}),
            'match2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quart_match2'", 'to': u"orm['tournoi.Match']"}),
            'match3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quart_match3'", 'to': u"orm['tournoi.Match']"}),
            'match4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quart_match4'", 'to': u"orm['tournoi.Match']"})
        },
        u'tournoi.seizieme': {
            'Meta': {'object_name': 'Seizieme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match1'", 'to': u"orm['tournoi.Match']"}),
            'match10': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match10'", 'to': u"orm['tournoi.Match']"}),
            'match11': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match11'", 'to': u"orm['tournoi.Match']"}),
            'match12': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match12'", 'to': u"orm['tournoi.Match']"}),
            'match13': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match13'", 'to': u"orm['tournoi.Match']"}),
            'match14': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match14'", 'to': u"orm['tournoi.Match']"}),
            'match15': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match15'", 'to': u"orm['tournoi.Match']"}),
            'match16': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match16'", 'to': u"orm['tournoi.Match']"}),
            'match2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match2'", 'to': u"orm['tournoi.Match']"}),
            'match3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match3'", 'to': u"orm['tournoi.Match']"}),
            'match4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match4'", 'to': u"orm['tournoi.Match']"}),
            'match5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match5'", 'to': u"orm['tournoi.Match']"}),
            'match6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match6'", 'to': u"orm['tournoi.Match']"}),
            'match7': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match7'", 'to': u"orm['tournoi.Match']"}),
            'match8': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match8'", 'to': u"orm['tournoi.Match']"}),
            'match9': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seizieme_match9'", 'to': u"orm['tournoi.Match']"})
        },
        u'tournoi.staff': {
            'Meta': {'object_name': 'Staff'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tournoi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tournoi.Tournoi']"})
        },
        u'tournoi.tournoi': {
            'Meta': {'object_name': 'Tournoi'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tournoi_admin'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'descr': ('django.db.models.fields.TextField', [], {}),
            'finale': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'heure': ('django.db.models.fields.TimeField', [], {'default': "'00:00:00'", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscrit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'loser_bracket': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'max_participants': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'poules': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regles': ('django.db.models.fields.TextField', [], {}),
            'termine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vainqueur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tournoi_vainqueur'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'tournoi.trentedeuxieme': {
            'Meta': {'object_name': 'Trentedeuxieme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match1'", 'to': u"orm['tournoi.Match']"}),
            'match10': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match10'", 'to': u"orm['tournoi.Match']"}),
            'match11': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match11'", 'to': u"orm['tournoi.Match']"}),
            'match12': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match12'", 'to': u"orm['tournoi.Match']"}),
            'match13': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match13'", 'to': u"orm['tournoi.Match']"}),
            'match14': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match14'", 'to': u"orm['tournoi.Match']"}),
            'match15': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match15'", 'to': u"orm['tournoi.Match']"}),
            'match16': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match16'", 'to': u"orm['tournoi.Match']"}),
            'match17': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match17'", 'to': u"orm['tournoi.Match']"}),
            'match18': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match18'", 'to': u"orm['tournoi.Match']"}),
            'match19': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match19'", 'to': u"orm['tournoi.Match']"}),
            'match2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match2'", 'to': u"orm['tournoi.Match']"}),
            'match20': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match20'", 'to': u"orm['tournoi.Match']"}),
            'match21': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match21'", 'to': u"orm['tournoi.Match']"}),
            'match22': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match22'", 'to': u"orm['tournoi.Match']"}),
            'match23': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match23'", 'to': u"orm['tournoi.Match']"}),
            'match24': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match24'", 'to': u"orm['tournoi.Match']"}),
            'match25': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match25'", 'to': u"orm['tournoi.Match']"}),
            'match26': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match26'", 'to': u"orm['tournoi.Match']"}),
            'match27': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match27'", 'to': u"orm['tournoi.Match']"}),
            'match28': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match28'", 'to': u"orm['tournoi.Match']"}),
            'match29': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match29'", 'to': u"orm['tournoi.Match']"}),
            'match3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match3'", 'to': u"orm['tournoi.Match']"}),
            'match30': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match30'", 'to': u"orm['tournoi.Match']"}),
            'match31': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match31'", 'to': u"orm['tournoi.Match']"}),
            'match32': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match32'", 'to': u"orm['tournoi.Match']"}),
            'match4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match4'", 'to': u"orm['tournoi.Match']"}),
            'match5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match5'", 'to': u"orm['tournoi.Match']"}),
            'match6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match6'", 'to': u"orm['tournoi.Match']"}),
            'match7': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match7'", 'to': u"orm['tournoi.Match']"}),
            'match8': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match8'", 'to': u"orm['tournoi.Match']"}),
            'match9': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trentedeuxieme_match9'", 'to': u"orm['tournoi.Match']"})
        }
    }

    complete_apps = ['tournoi']