# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Abuse.timestamp'
        db.delete_column(u'misc_abuse', 'timestamp')

        # Adding field 'Abuse.created'
        db.add_column(u'misc_abuse', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'CheckPoint.date'
        db.delete_column(u'misc_checkpoint', 'date')

        # Adding field 'CheckPoint.created'
        db.add_column(u'misc_checkpoint', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Abuse.timestamp'
        db.add_column(u'misc_abuse', 'timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Abuse.created'
        db.delete_column(u'misc_abuse', 'created')

        # Adding field 'CheckPoint.date'
        db.add_column(u'misc_checkpoint', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'CheckPoint.created'
        db.delete_column(u'misc_checkpoint', 'created')


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
            'lat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'migrante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Migrant']"}),
            'other_location': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'pseudo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['misc']