# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CheckPoint.lon'
        db.alter_column(u'misc_checkpoint', 'lon', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'CheckPoint.lat'
        db.alter_column(u'misc_checkpoint', 'lat', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'CheckPoint.other_location'
        db.alter_column(u'misc_checkpoint', 'other_location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Adding field 'Migrant.origin_lat'
        db.add_column(u'misc_migrant', 'origin_lat',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Migrant.origin_lng'
        db.add_column(u'misc_migrant', 'origin_lng',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'CheckPoint.lon'
        db.alter_column(u'misc_checkpoint', 'lon', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CheckPoint.lat'
        db.alter_column(u'misc_checkpoint', 'lat', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CheckPoint.other_location'
        db.alter_column(u'misc_checkpoint', 'other_location', self.gf('django.db.models.fields.IntegerField')())
        # Deleting field 'Migrant.origin_lat'
        db.delete_column(u'misc_migrant', 'origin_lat')

        # Deleting field 'Migrant.origin_lng'
        db.delete_column(u'misc_migrant', 'origin_lng')


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
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'martial': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '15'}),
            'origin_lat': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'origin_lng': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['misc']