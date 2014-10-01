# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'model2'
        db.create_table('myapp_model2', (
            ('name1', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('myapp', ['model2'])

        # Adding model 'model1'
        db.create_table('myapp_model1', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('many', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('myapp', ['model1'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'model2'
        db.delete_table('myapp_model2')

        # Deleting model 'model1'
        db.delete_table('myapp_model1')
    
    
    models = {
        'myapp.model1': {
            'Meta': {'object_name': 'model1'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'many': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'myapp.model2': {
            'Meta': {'object_name': 'model2'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name1': ('django.db.models.fields.IntegerField', [], {})
        }
    }
    
    complete_apps = ['myapp']
