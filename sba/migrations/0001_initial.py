# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table('sba_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('sba', ['Region'])

        # Adding model 'Topic'
        db.create_table('sba_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('sba', ['Topic'])

        # Adding model 'SearchTerm'
        db.create_table('sba_searchterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('sba', ['SearchTerm'])

        # Adding model 'lnkTopicTerm'
        db.create_table('sba_lnktopicterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('top', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Topic'])),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.SearchTerm'])),
        ))
        db.send_create_signal('sba', ['lnkTopicTerm'])

        # Adding model 'lnkRegTopic'
        db.create_table('sba_lnkregtopic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Region'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Topic'])),
        ))
        db.send_create_signal('sba', ['lnkRegTopic'])

        # Adding model 'RegionalOccurrence'
        db.create_table('sba_regionaloccurrence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Region'])),
            ('termtop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.lnkTopicTerm'])),
            ('occurs', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('sba', ['RegionalOccurrence'])

        # Adding model 'Tweet'
        db.create_table('sba_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('reg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Region'])),
        ))
        db.send_create_signal('sba', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table('sba_region')

        # Deleting model 'Topic'
        db.delete_table('sba_topic')

        # Deleting model 'SearchTerm'
        db.delete_table('sba_searchterm')

        # Deleting model 'lnkTopicTerm'
        db.delete_table('sba_lnktopicterm')

        # Deleting model 'lnkRegTopic'
        db.delete_table('sba_lnkregtopic')

        # Deleting model 'RegionalOccurrence'
        db.delete_table('sba_regionaloccurrence')

        # Deleting model 'Tweet'
        db.delete_table('sba_tweet')


    models = {
        'sba.lnkregtopic': {
            'Meta': {'object_name': 'lnkRegTopic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.Region']"}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.Topic']"})
        },
        'sba.lnktopicterm': {
            'Meta': {'object_name': 'lnkTopicTerm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.SearchTerm']"}),
            'top': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.Topic']"})
        },
        'sba.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sba.regionaloccurrence': {
            'Meta': {'object_name': 'RegionalOccurrence'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.Region']"}),
            'termtop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.lnkTopicTerm']"})
        },
        'sba.searchterm': {
            'Meta': {'object_name': 'SearchTerm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'sba.topic': {
            'Meta': {'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sba.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.Region']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['sba']