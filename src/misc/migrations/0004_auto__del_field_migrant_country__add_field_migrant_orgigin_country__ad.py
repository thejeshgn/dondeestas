# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Migrant.country'
        db.delete_column(u'misc_migrant', 'country')

        # Adding field 'Migrant.orgigin_country'
        db.add_column(u'misc_migrant', 'orgigin_country',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Migrant.dest_country'
        db.add_column(u'misc_migrant', 'dest_country',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Migrant.dest_lat'
        db.add_column(u'misc_migrant', 'dest_lat',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Migrant.dest_lng'
        db.add_column(u'misc_migrant', 'dest_lng',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Migrant.country'
        raise RuntimeError("Cannot reverse this migration. 'Migrant.country' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Migrant.country'
        db.add_column(u'misc_migrant', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)

        # Deleting field 'Migrant.orgigin_country'
        db.delete_column(u'misc_migrant', 'orgigin_country')

        # Deleting field 'Migrant.dest_country'
        db.delete_column(u'misc_migrant', 'dest_country')

        # Deleting field 'Migrant.dest_lat'
        db.delete_column(u'misc_migrant', 'dest_lat')

        # Deleting field 'Migrant.dest_lng'
        db.delete_column(u'misc_migrant', 'dest_lng')


    models = {
        u'misc.abuse': {
            'Meta': {'object_name': 'Abuse'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'migrante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Migrant']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Others'", 'max_length': '100'})
        },
        u'misc.checkpoint': {
            'Meta': {'object_name': 'CheckPoint'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'migrante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Migrant']"}),
            'other_location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'misc.migrant': {
            'Meta': {'object_name': 'Migrant'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dest_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dest_lat': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'dest_lng': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'martial': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '15'}),
            'orgigin_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'origin_lat': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'origin_lng': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['misc']