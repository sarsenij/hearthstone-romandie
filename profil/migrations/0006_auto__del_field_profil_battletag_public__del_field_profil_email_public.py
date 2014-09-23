# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Profil.battletag_public'
        db.delete_column('profil_profil', 'battletag_public')

        # Deleting field 'Profil.email_public'
        db.delete_column('profil_profil', 'email_public')

        # Deleting field 'Profil.localite_contact'
        db.delete_column('profil_profil', 'localite_contact')

        # Deleting field 'Profil.telephone_contact'
        db.delete_column('profil_profil', 'telephone_contact')

        # Deleting field 'Profil.battletag_contact'
        db.delete_column('profil_profil', 'battletag_contact')

        # Deleting field 'Profil.ville_proche_contact'
        db.delete_column('profil_profil', 'ville_proche_contact')

        # Deleting field 'Profil.nom_contact'
        db.delete_column('profil_profil', 'nom_contact')

        # Deleting field 'Profil.localite_public'
        db.delete_column('profil_profil', 'localite_public')

        # Deleting field 'Profil.nom_public'
        db.delete_column('profil_profil', 'nom_public')

        # Deleting field 'Profil.ville_proche_public'
        db.delete_column('profil_profil', 'ville_proche_public')

        # Deleting field 'Profil.telephone_public'
        db.delete_column('profil_profil', 'telephone_public')

        # Deleting field 'Profil.email_contact'
        db.delete_column('profil_profil', 'email_contact')

        # Deleting field 'Profil.prenom_contact'
        db.delete_column('profil_profil', 'prenom_contact')

        # Deleting field 'Profil.prenom_public'
        db.delete_column('profil_profil', 'prenom_public')

        # Deleting field 'Profil.rue_contact'
        db.delete_column('profil_profil', 'rue_contact')

        # Deleting field 'Profil.rue_public'
        db.delete_column('profil_profil', 'rue_public')

        # Adding field 'Profil.nom_privacy'
        db.add_column('profil_profil', 'nom_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profil.prenom_privacy'
        db.add_column('profil_profil', 'prenom_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profil.email_privacy'
        db.add_column('profil_profil', 'email_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profil.rue_privacy'
        db.add_column('profil_profil', 'rue_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profil.localite_privacy'
        db.add_column('profil_profil', 'localite_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profil.ville_proche_privacy'
        db.add_column('profil_profil', 'ville_proche_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profil.battletag_privacy'
        db.add_column('profil_profil', 'battletag_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profil.telephone_privacy'
        db.add_column('profil_profil', 'telephone_privacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Profil.battletag_public'
        db.add_column('profil_profil', 'battletag_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.email_public'
        db.add_column('profil_profil', 'email_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.localite_contact'
        db.add_column('profil_profil', 'localite_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.telephone_contact'
        db.add_column('profil_profil', 'telephone_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.battletag_contact'
        db.add_column('profil_profil', 'battletag_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.ville_proche_contact'
        db.add_column('profil_profil', 'ville_proche_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.nom_contact'
        db.add_column('profil_profil', 'nom_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.localite_public'
        db.add_column('profil_profil', 'localite_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.nom_public'
        db.add_column('profil_profil', 'nom_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.ville_proche_public'
        db.add_column('profil_profil', 'ville_proche_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.telephone_public'
        db.add_column('profil_profil', 'telephone_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.email_contact'
        db.add_column('profil_profil', 'email_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.prenom_contact'
        db.add_column('profil_profil', 'prenom_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.prenom_public'
        db.add_column('profil_profil', 'prenom_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.rue_contact'
        db.add_column('profil_profil', 'rue_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.rue_public'
        db.add_column('profil_profil', 'rue_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Profil.nom_privacy'
        db.delete_column('profil_profil', 'nom_privacy')

        # Deleting field 'Profil.prenom_privacy'
        db.delete_column('profil_profil', 'prenom_privacy')

        # Deleting field 'Profil.email_privacy'
        db.delete_column('profil_profil', 'email_privacy')

        # Deleting field 'Profil.rue_privacy'
        db.delete_column('profil_profil', 'rue_privacy')

        # Deleting field 'Profil.localite_privacy'
        db.delete_column('profil_profil', 'localite_privacy')

        # Deleting field 'Profil.ville_proche_privacy'
        db.delete_column('profil_profil', 'ville_proche_privacy')

        # Deleting field 'Profil.battletag_privacy'
        db.delete_column('profil_profil', 'battletag_privacy')

        # Deleting field 'Profil.telephone_privacy'
        db.delete_column('profil_profil', 'telephone_privacy')


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
        'profil.profil': {
            'Meta': {'object_name': 'Profil'},
            'battletag': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'battletag_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'email_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profil.Localite']", 'null': 'True', 'blank': 'True'}),
            'localite_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'nom_privacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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