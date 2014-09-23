# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VilleProche'
        db.create_table('profil_villeproche', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ville_proche', self.gf('django.db.models.fields.CharField')(max_length=125)),
        ))
        db.send_create_signal('profil', ['VilleProche'])

        # Adding field 'Profil.ville_proche'
        db.add_column('profil_profil', 'ville_proche',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profil.VilleProche'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profil.ville_proche_contact'
        db.add_column('profil_profil', 'ville_proche_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.ville_proche_public'
        db.add_column('profil_profil', 'ville_proche_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'VilleProche'
        db.delete_table('profil_villeproche')

        # Deleting field 'Profil.ville_proche'
        db.delete_column('profil_profil', 'ville_proche_id')

        # Deleting field 'Profil.ville_proche_contact'
        db.delete_column('profil_profil', 'ville_proche_contact')

        # Deleting field 'Profil.ville_proche_public'
        db.delete_column('profil_profil', 'ville_proche_public')


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
        'profil.localite': {
            'Meta': {'object_name': 'Localite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localite': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        },
        'profil.profil': {
            'Meta': {'object_name': 'Profil'},
            'battletag': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'battletag_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'battletag_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'email_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profil.Localite']", 'null': 'True', 'blank': 'True'}),
            'localite_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'localite_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'nom_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nom_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'prenom_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prenom_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'rue': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'rue_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rue_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'telephone_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telephone_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'u': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'ville_proche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profil.VilleProche']", 'null': 'True', 'blank': 'True'}),
            'ville_proche_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ville_proche_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'profil.villeproche': {
            'Meta': {'object_name': 'VilleProche'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ville_proche': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        }
    }

    complete_apps = ['profil']