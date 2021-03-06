# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Attachment.name'
        db.delete_column('judge_attachment', 'name')

        # Deleting field 'Attachment.path'
        db.delete_column('judge_attachment', 'path')

        # Deleting field 'Attachment.size'
        db.delete_column('judge_attachment', 'size')

        # Deleting field 'Attachment.md5'
        db.delete_column('judge_attachment', 'md5')

        # Adding field 'Attachment.file'
        db.add_column('judge_attachment', 'file', self.gf('django.db.models.fields.files.FileField')(default='argh', max_length=1024), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Attachment.name'
        db.add_column('judge_attachment', 'name', self.gf('django.db.models.fields.CharField')(default='meh', max_length=128), keep_default=False)

        # Adding field 'Attachment.path'
        db.add_column('judge_attachment', 'path', self.gf('django.db.models.fields.CharField')(default='bah', max_length=256), keep_default=False)

        # Adding field 'Attachment.size'
        db.add_column('judge_attachment', 'size', self.gf('django.db.models.fields.IntegerField')(default='dah'), keep_default=False)

        # Adding field 'Attachment.md5'
        db.add_column('judge_attachment', 'md5', self.gf('django.db.models.fields.CharField')(default='gah', max_length=32), keep_default=False)

        # Deleting field 'Attachment.file'
        db.delete_column('judge_attachment', 'file')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'judge.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['judge.Problem']"})
        },
        'judge.problem': {
            'Meta': {'object_name': 'Problem'},
            'accepted_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'judge_module': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'memory_limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '65536'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'output': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sample_input': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sample_output': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'submissions_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time_limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10000'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'judge.submission': {
            'Meta': {'object_name': 'Submission'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'memory': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['judge.Problem']"}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'submitted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['judge']
