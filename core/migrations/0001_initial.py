# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'core_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('brief_description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'core_item')


    models = {
        u'core.item': {
            'Meta': {'object_name': 'Item'},
            'brief_description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']"}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['core']