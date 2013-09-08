# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SearchTerm.topic'
        db.add_column('sba_searchterm', 'topic',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['sba.Topic']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SearchTerm.topic'
        db.delete_column('sba_searchterm', 'topic_id')


    models = {
        'sba.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sba.searchterm': {
            'Meta': {'object_name': 'SearchTerm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sba.Topic']"})
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