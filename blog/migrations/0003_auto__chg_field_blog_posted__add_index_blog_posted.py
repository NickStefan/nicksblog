# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Blog.posted'
        db.alter_column('blog_blog', 'posted', self.gf('django.db.models.fields.DateTimeField')())
        # Adding index on 'Blog', fields ['posted']
        db.create_index('blog_blog', ['posted'])


    def backwards(self, orm):
        # Removing index on 'Blog', fields ['posted']
        db.delete_index('blog_blog', ['posted'])


        # Changing field 'Blog.posted'
        db.alter_column('blog_blog', 'posted', self.gf('django.db.models.fields.TextField')())

    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Category']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['blog']