# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Message.owner'
        db.alter_column(u'notification_message', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Destinataire.destinataire'
        db.alter_column(u'notification_destinataire', 'destinataire_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'MessageVu.destinataire'
        db.alter_column(u'notification_messagevu', 'destinataire_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):

        # Changing field 'Message.owner'
        db.alter_column(u'notification_message', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profil.Profil']))

        # Changing field 'Destinataire.destinataire'
        db.alter_column(u'notification_destinataire', 'destinataire_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profil.Profil']))

        # Changing field 'MessageVu.destinataire'
        db.alter_column(u'notification_messagevu', 'destinataire_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profil.Profil']))

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
        u'notification.destinataire': {
            'Meta': {'object_name': 'Destinataire'},
            'destinataire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destinataire'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messagetitre': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destinataires'", 'null': 'True', 'to': u"orm['notification.MessageTitre']"})
        },
        u'notification.message': {
            'Meta': {'object_name': 'Message'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'titre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notification.MessageTitre']"})
        },
        u'notification.messagetitre': {
            'Meta': {'object_name': 'MessageTitre'},
            'edit': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'notification.messagevu': {
            'Meta': {'object_name': 'MessageVu'},
            'destinataire': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notification.Message']"}),
            'messagetitre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notification.MessageTitre']", 'null': 'True'}),
            'vu': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'notification.notification': {
            'Meta': {'object_name': 'Notification'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profil.Contact']", 'null': 'True', 'blank': 'True'}),
            'contact_already': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'destinataire': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profil.Profil']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notification.Message']", 'null': 'True', 'blank': 'True'}),
            'vue': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'profil.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact'", 'to': u"orm['profil.Profil']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': u"orm['profil.Profil']"})
        },
        u'profil.localite': {
            'Meta': {'object_name': 'Localite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localite': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        u'profil.pays': {
            'Meta': {'object_name': 'Pays'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        u'profil.profil': {
            'Meta': {'object_name': 'Profil'},
            'avatar': ('django.db.models.fields.CharField', [], {'default': "'/static/images/avatars/avatar.png'", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'battletag': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'battletag_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'email_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localite': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['profil.Localite']", 'null': 'True', 'blank': 'True'}),
            'localite_privacy': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'nom_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['profil.Pays']", 'null': 'True', 'blank': 'True'}),
            'pays_privacy': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'prenom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'prenom_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'rue': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'rue_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'telephone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'telephone_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'u': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'ville_proche': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['profil.VilleProche']", 'null': 'True', 'blank': 'True'}),
            'ville_proche_privacy': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        u'profil.villeproche': {
            'Meta': {'object_name': 'VilleProche'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ville_proche': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        }
    }

    complete_apps = ['notification']