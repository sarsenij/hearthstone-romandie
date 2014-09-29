# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Arbre'
        db.delete_table(u'tournoi_arbre')

        # Deleting model 'Poule'
        db.delete_table(u'tournoi_poule')

        # Deleting model 'Seizieme'
        db.delete_table(u'tournoi_seizieme')

        # Deleting model 'Trentedeuxieme'
        db.delete_table(u'tournoi_trentedeuxieme')

        # Deleting model 'Quart'
        db.delete_table(u'tournoi_quart')

        # Deleting model 'Huitieme'
        db.delete_table(u'tournoi_huitieme')

        # Deleting model 'DemiFinale'
        db.delete_table(u'tournoi_demifinale')

        # Deleting field 'Match.first_freewin'
        db.delete_column(u'tournoi_match', 'first_freewin')

        # Deleting field 'Match.second_freewin'
        db.delete_column(u'tournoi_match', 'second_freewin')

        # Adding field 'Match.tournoi'
        db.add_column(u'tournoi_match', 'tournoi',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='tournoi_match', null=True, to=orm['tournoi.Tournoi']),
                      keep_default=False)

        # Adding field 'Match.freewin'
        db.add_column(u'tournoi_match', 'freewin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Match.next_gagnant'
        db.add_column(u'tournoi_match', 'next_gagnant',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='Match_next_gagnant', null=True, to=orm['tournoi.Match']),
                      keep_default=False)

        # Adding field 'Match.next_perdant'
        db.add_column(u'tournoi_match', 'next_perdant',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='Match_next_perdant', null=True, to=orm['tournoi.Match']),
                      keep_default=False)

        # Adding field 'Match.col'
        db.add_column(u'tournoi_match', 'col',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Match.row'
        db.add_column(u'tournoi_match', 'row',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Match.valide'
        db.add_column(u'tournoi_match', 'valide',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Match.score_first'
        db.alter_column(u'tournoi_match', 'score_first', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.score_second'
        db.alter_column(u'tournoi_match', 'score_second', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Adding model 'Arbre'
        db.create_table(u'tournoi_arbre', (
            ('demifinale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournoi.DemiFinale'], null=True)),
            ('seizieme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournoi.Seizieme'], null=True)),
            ('petitefinale', self.gf('django.db.models.fields.related.ForeignKey')(related_name='petitefinale', null=True, to=orm['tournoi.Match'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('huitieme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournoi.Huitieme'], null=True)),
            ('poule11', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule11', null=True, to=orm['tournoi.Poule'])),
            ('poule10', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule10', null=True, to=orm['tournoi.Poule'])),
            ('poule13', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule13', null=True, to=orm['tournoi.Poule'])),
            ('poule12', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule12', null=True, to=orm['tournoi.Poule'])),
            ('poule15', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule15', null=True, to=orm['tournoi.Poule'])),
            ('poule14', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule14', null=True, to=orm['tournoi.Poule'])),
            ('poule16', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule16', null=True, to=orm['tournoi.Poule'])),
            ('finale', self.gf('django.db.models.fields.related.ForeignKey')(related_name='finale', null=True, to=orm['tournoi.Match'])),
            ('tournoi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournoi.Tournoi'])),
            ('quart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournoi.Quart'], null=True)),
            ('poule9', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule9', null=True, to=orm['tournoi.Poule'])),
            ('poule8', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule8', null=True, to=orm['tournoi.Poule'])),
            ('poule5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule5', null=True, to=orm['tournoi.Poule'])),
            ('poule4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule4', null=True, to=orm['tournoi.Poule'])),
            ('poule7', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule7', null=True, to=orm['tournoi.Poule'])),
            ('poule6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule6', null=True, to=orm['tournoi.Poule'])),
            ('poule1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule1', null=True, to=orm['tournoi.Poule'])),
            ('poule3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule3', null=True, to=orm['tournoi.Poule'])),
            ('poule2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule2', null=True, to=orm['tournoi.Poule'])),
            ('trentedeuxieme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournoi.Trentedeuxieme'], null=True)),
            ('finale_loser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='finale_loser', null=True, to=orm['tournoi.Match'])),
        ))
        db.send_create_signal(u'tournoi', ['Arbre'])

        # Adding model 'Poule'
        db.create_table(u'tournoi_poule', (
            ('match6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule_match6', to=orm['tournoi.Match'])),
            ('match5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule_match5', to=orm['tournoi.Match'])),
            ('match3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule_match3', to=orm['tournoi.Match'])),
            ('match2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule_match2', to=orm['tournoi.Match'])),
            ('match1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule_match1', to=orm['tournoi.Match'])),
            ('match4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poule_match4', to=orm['tournoi.Match'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tournoi', ['Poule'])

        # Adding model 'Seizieme'
        db.create_table(u'tournoi_seizieme', (
            ('match7', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match7', to=orm['tournoi.Match'])),
            ('match6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match6', to=orm['tournoi.Match'])),
            ('match5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match5', to=orm['tournoi.Match'])),
            ('match4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match4', to=orm['tournoi.Match'])),
            ('match3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match3', to=orm['tournoi.Match'])),
            ('match2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match2', to=orm['tournoi.Match'])),
            ('match1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match1', to=orm['tournoi.Match'])),
            ('match9', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match9', to=orm['tournoi.Match'])),
            ('match14', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match14', to=orm['tournoi.Match'])),
            ('match16', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match16', to=orm['tournoi.Match'])),
            ('match15', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match15', to=orm['tournoi.Match'])),
            ('match13', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match13', to=orm['tournoi.Match'])),
            ('match12', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match12', to=orm['tournoi.Match'])),
            ('match11', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match11', to=orm['tournoi.Match'])),
            ('match10', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match10', to=orm['tournoi.Match'])),
            ('match8', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seizieme_match8', to=orm['tournoi.Match'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tournoi', ['Seizieme'])

        # Adding model 'Trentedeuxieme'
        db.create_table(u'tournoi_trentedeuxieme', (
            ('match7', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match7', to=orm['tournoi.Match'])),
            ('match6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match6', to=orm['tournoi.Match'])),
            ('match5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match5', to=orm['tournoi.Match'])),
            ('match4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match4', to=orm['tournoi.Match'])),
            ('match3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match3', to=orm['tournoi.Match'])),
            ('match2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match2', to=orm['tournoi.Match'])),
            ('match1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match1', to=orm['tournoi.Match'])),
            ('match29', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match29', to=orm['tournoi.Match'])),
            ('match9', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match9', to=orm['tournoi.Match'])),
            ('match8', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match8', to=orm['tournoi.Match'])),
            ('match32', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match32', to=orm['tournoi.Match'])),
            ('match20', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match20', to=orm['tournoi.Match'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match31', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match31', to=orm['tournoi.Match'])),
            ('match25', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match25', to=orm['tournoi.Match'])),
            ('match30', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match30', to=orm['tournoi.Match'])),
            ('match28', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match28', to=orm['tournoi.Match'])),
            ('match14', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match14', to=orm['tournoi.Match'])),
            ('match17', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match17', to=orm['tournoi.Match'])),
            ('match16', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match16', to=orm['tournoi.Match'])),
            ('match15', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match15', to=orm['tournoi.Match'])),
            ('match13', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match13', to=orm['tournoi.Match'])),
            ('match12', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match12', to=orm['tournoi.Match'])),
            ('match11', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match11', to=orm['tournoi.Match'])),
            ('match10', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match10', to=orm['tournoi.Match'])),
            ('match26', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match26', to=orm['tournoi.Match'])),
            ('match27', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match27', to=orm['tournoi.Match'])),
            ('match24', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match24', to=orm['tournoi.Match'])),
            ('match21', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match21', to=orm['tournoi.Match'])),
            ('match22', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match22', to=orm['tournoi.Match'])),
            ('match23', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match23', to=orm['tournoi.Match'])),
            ('match19', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match19', to=orm['tournoi.Match'])),
            ('match18', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trentedeuxieme_match18', to=orm['tournoi.Match'])),
        ))
        db.send_create_signal(u'tournoi', ['Trentedeuxieme'])

        # Adding model 'Quart'
        db.create_table(u'tournoi_quart', (
            ('match4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quart_match4', to=orm['tournoi.Match'])),
            ('match3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quart_match3', to=orm['tournoi.Match'])),
            ('match2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quart_match2', to=orm['tournoi.Match'])),
            ('match1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quart_match1', to=orm['tournoi.Match'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tournoi', ['Quart'])

        # Adding model 'Huitieme'
        db.create_table(u'tournoi_huitieme', (
            ('match7', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match7', to=orm['tournoi.Match'])),
            ('match6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match6', to=orm['tournoi.Match'])),
            ('match5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match5', to=orm['tournoi.Match'])),
            ('match3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match3', to=orm['tournoi.Match'])),
            ('match2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match2', to=orm['tournoi.Match'])),
            ('match1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match1', to=orm['tournoi.Match'])),
            ('match4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match4', to=orm['tournoi.Match'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match8', self.gf('django.db.models.fields.related.ForeignKey')(related_name='huitieme_match8', to=orm['tournoi.Match'])),
        ))
        db.send_create_signal(u'tournoi', ['Huitieme'])

        # Adding model 'DemiFinale'
        db.create_table(u'tournoi_demifinale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='demifinale_match1', to=orm['tournoi.Match'])),
            ('match2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='demifinale_match2', to=orm['tournoi.Match'])),
        ))
        db.send_create_signal(u'tournoi', ['DemiFinale'])

        # Adding field 'Match.first_freewin'
        db.add_column(u'tournoi_match', 'first_freewin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Match.second_freewin'
        db.add_column(u'tournoi_match', 'second_freewin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Match.tournoi'
        db.delete_column(u'tournoi_match', 'tournoi_id')

        # Deleting field 'Match.freewin'
        db.delete_column(u'tournoi_match', 'freewin')

        # Deleting field 'Match.next_gagnant'
        db.delete_column(u'tournoi_match', 'next_gagnant_id')

        # Deleting field 'Match.next_perdant'
        db.delete_column(u'tournoi_match', 'next_perdant_id')

        # Deleting field 'Match.col'
        db.delete_column(u'tournoi_match', 'col')

        # Deleting field 'Match.row'
        db.delete_column(u'tournoi_match', 'row')

        # Deleting field 'Match.valide'
        db.delete_column(u'tournoi_match', 'valide')


        # Changing field 'Match.score_first'
        db.alter_column(u'tournoi_match', 'score_first', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.score_second'
        db.alter_column(u'tournoi_match', 'score_second', self.gf('django.db.models.fields.IntegerField')())

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
            'col': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'first': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'first_match'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'freewin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_gagnant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Match_next_gagnant'", 'null': 'True', 'to': u"orm['tournoi.Match']"}),
            'next_perdant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Match_next_perdant'", 'null': 'True', 'to': u"orm['tournoi.Match']"}),
            'row': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_first': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'score_first_by_first': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_first_by_second': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_second': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'score_second_by_first': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_second_by_second': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'second': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'second_match'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'tournoi': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tournoi_match'", 'null': 'True', 'to': u"orm['tournoi.Tournoi']"}),
            'valide': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        }
    }

    complete_apps = ['tournoi']