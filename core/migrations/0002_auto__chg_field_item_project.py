# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.project'
        db.alter_column(u'core_item', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Item.project'
        raise RuntimeError("Cannot reverse this migration. 'Item.project' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Item.project'
        db.alter_column(u'core_item', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Item']))

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
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Item']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['core']