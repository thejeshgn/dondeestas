# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Migrant'
        db.create_table(u'misc_migrant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pseudo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=15)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('martial', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=15)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'misc', ['Migrant'])

        # Adding model 'Abuse'
        db.create_table(u'misc_abuse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='Others', max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('migrante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Migrant'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'misc', ['Abuse'])

        # Adding model 'CheckPoint'
        db.create_table(u'misc_checkpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('migrante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.Migrant'])),
            ('lon', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('lat', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('other_location', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'misc', ['CheckPoint'])


    def backwards(self, orm):
        # Deleting model 'Migrant'
        db.delete_table(u'misc_migrant')

        # Deleting model 'Abuse'
        db.delete_table(u'misc_abuse')

        # Deleting model 'CheckPoint'
        db.delete_table(u'misc_checkpoint')


    models = {
        u'misc.abuse': {
            'Meta': {'object_name': 'Abuse'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'migrante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.Migrant']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Others'", 'max_length': '100'})
        },
        u'misc.checkpoint': {
            'Meta': {'object_name': 'CheckPoint'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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