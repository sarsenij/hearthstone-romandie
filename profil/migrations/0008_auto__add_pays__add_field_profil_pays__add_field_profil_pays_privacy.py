# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pays'
        db.create_table('profil_pays', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pays', self.gf('django.db.models.fields.CharField')(max_length=125)),
        ))
        db.send_create_signal('profil', ['Pays'])

        # Adding field 'Profil.pays'
        db.add_column('profil_profil', 'pays',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profil.Pays'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profil.pays_privacy'
        db.add_column('profil_profil', 'pays_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Pays'
        db.delete_table('profil_pays')

        # Deleting field 'Profil.pays'
        db.delete_column('profil_profil', 'pays_id')

        # Deleting field 'Profil.pays_privacy'
        db.delete_column('profil_profil', 'pays_privacy')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profil.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact'", 'to': "orm['profil.Profil']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': "orm['profil.Profil']"})
        },
        'profil.localite': {
            'Meta': {'object_name': 'Localite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localite': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        'profil.pays': {
            'Meta': {'object_name': 'Pays'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        'profil.profil': {
            'Meta': {'object_name': 'Profil'},
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'battletag': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'battletag_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'email_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profil.Localite']", 'null': 'True', 'blank': 'True'}),
            'localite_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'nom_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profil.Pays']", 'null': 'True', 'blank': 'True'}),
            'pays_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'prenom_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'rue': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'rue_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'telephone_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'u': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'ville_proche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profil.VilleProche']", 'null': 'True', 'blank': 'True'}),
            'ville_proche_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'profil.villeproche': {
            'Meta': {'object_name': 'VilleProche'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ville_proche': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        }
    }

    complete_apps = ['profil']