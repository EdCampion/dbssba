# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RegionalOccurrence'
        db.delete_table('sba_regionaloccurrence')

        # Deleting model 'lnkTopicTerm'
        db.delete_table('sba_lnktopicterm')

        # Deleting model 'lnkRegTopic'
        db.delete_table('sba_lnkregtopic')


    def backwards(self, orm):
        # Adding model 'RegionalOccurrence'
        db.create_table('sba_regionaloccurrence', (
            ('termtop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.lnkTopicTerm'])),
            ('reg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Region'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('occurs', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('sba', ['RegionalOccurrence'])

        # Adding model 'lnkTopicTerm'
        db.create_table('sba_lnktopicterm', (
            ('top', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Topic'])),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.SearchTerm'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('sba', ['lnkTopicTerm'])

        # Adding model 'lnkRegTopic'
        db.create_table('sba_lnkregtopic', (
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Topic'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sba.Region'])),
        ))
        db.send_create_signal('sba', ['lnkRegTopic'])


    models = {
        'sba.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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