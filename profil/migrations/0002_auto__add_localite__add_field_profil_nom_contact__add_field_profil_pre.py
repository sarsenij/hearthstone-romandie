# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Localite'
        db.create_table('profil_localite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('localite', self.gf('django.db.models.fields.CharField')(max_length=125)),
        ))
        db.send_create_signal('profil', ['Localite'])

        # Adding field 'Profil.nom_contact'
        db.add_column('profil_profil', 'nom_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.prenom_contact'
        db.add_column('profil_profil', 'prenom_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.email'
        db.add_column('profil_profil', 'email',
                      self.gf('django.db.models.fields.CharField')(default='caca', max_length=125),
                      keep_default=False)

        # Adding field 'Profil.email_contact'
        db.add_column('profil_profil', 'email_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.email_public'
        db.add_column('profil_profil', 'email_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.rue'
        db.add_column('profil_profil', 'rue',
                      self.gf('django.db.models.fields.CharField')(max_length=125, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profil.rue_contact'
        db.add_column('profil_profil', 'rue_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.rue_public'
        db.add_column('profil_profil', 'rue_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.localite'
        db.add_column('profil_profil', 'localite',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profil.Localite'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profil.localite_contact'
        db.add_column('profil_profil', 'localite_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.localite_public'
        db.add_column('profil_profil', 'localite_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.battletag'
        db.add_column('profil_profil', 'battletag',
                      self.gf('django.db.models.fields.CharField')(max_length=125, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profil.battletag_contact'
        db.add_column('profil_profil', 'battletag_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.battletag_public'
        db.add_column('profil_profil', 'battletag_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.telephone'
        db.add_column('profil_profil', 'telephone',
                      self.gf('django.db.models.fields.CharField')(max_length=125, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Profil.telephone_contact'
        db.add_column('profil_profil', 'telephone_contact',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Profil.telephone_public'
        db.add_column('profil_profil', 'telephone_public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Profil.nom'
        db.alter_column('profil_profil', 'nom', self.gf('django.db.models.fields.CharField')(max_length=125, null=True))

        # Changing field 'Profil.prenom'
        db.alter_column('profil_profil', 'prenom', self.gf('django.db.models.fields.CharField')(max_length=125, null=True))

    def backwards(self, orm):
        # Deleting model 'Localite'
        db.delete_table('profil_localite')

        # Deleting field 'Profil.nom_contact'
        db.delete_column('profil_profil', 'nom_contact')

        # Deleting field 'Profil.prenom_contact'
        db.delete_column('profil_profil', 'prenom_contact')

        # Deleting field 'Profil.email'
        db.delete_column('profil_profil', 'email')

        # Deleting field 'Profil.email_contact'
        db.delete_column('profil_profil', 'email_contact')

        # Deleting field 'Profil.email_public'
        db.delete_column('profil_profil', 'email_public')

        # Deleting field 'Profil.rue'
        db.delete_column('profil_profil', 'rue')

        # Deleting field 'Profil.rue_contact'
        db.delete_column('profil_profil', 'rue_contact')

        # Deleting field 'Profil.rue_public'
        db.delete_column('profil_profil', 'rue_public')

        # Deleting field 'Profil.localite'
        db.delete_column('profil_profil', 'localite_id')

        # Deleting field 'Profil.localite_contact'
        db.delete_column('profil_profil', 'localite_contact')

        # Deleting field 'Profil.localite_public'
        db.delete_column('profil_profil', 'localite_public')

        # Deleting field 'Profil.battletag'
        db.delete_column('profil_profil', 'battletag')

        # Deleting field 'Profil.battletag_contact'
        db.delete_column('profil_profil', 'battletag_contact')

        # Deleting field 'Profil.battletag_public'
        db.delete_column('profil_profil', 'battletag_public')

        # Deleting field 'Profil.telephone'
        db.delete_column('profil_profil', 'telephone')

        # Deleting field 'Profil.telephone_contact'
        db.delete_column('profil_profil', 'telephone_contact')

        # Deleting field 'Profil.telephone_public'
        db.delete_column('profil_profil', 'telephone_public')


        # User chose to not deal with backwards NULL issues for 'Profil.nom'
        raise RuntimeError("Cannot reverse this migration. 'Profil.nom' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Profil.prenom'
        raise RuntimeError("Cannot reverse this migration. 'Profil.prenom' and its values cannot be restored.")

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
            'rue': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'rue_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rue_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'telephone_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telephone_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'u': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['profil']