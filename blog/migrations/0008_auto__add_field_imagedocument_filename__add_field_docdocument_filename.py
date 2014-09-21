# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ImageDocument.filename'
        db.add_column('blog_imagedocument', 'filename',
                      self.gf('django.db.models.fields.CharField')(default='file', max_length=150),
                      keep_default=False)

        # Adding field 'DocDocument.filename'
        db.add_column('blog_docdocument', 'filename',
                      self.gf('django.db.models.fields.CharField')(default='file', max_length=150),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ImageDocument.filename'
        db.delete_column('blog_imagedocument', 'filename')

        # Deleting field 'DocDocument.filename'
        db.delete_column('blog_docdocument', 'filename')


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Category']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'blog.docdocument': {
            'Meta': {'object_name': 'DocDocument'},
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'blog.imagedocument': {
            'Meta': {'object_name': 'ImageDocument'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']