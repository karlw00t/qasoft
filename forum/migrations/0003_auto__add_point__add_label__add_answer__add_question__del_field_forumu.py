# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Point'
        db.create_table('forum_point', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('fromuser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('forum', ['Point'])

        # Adding model 'Label'
        db.create_table('forum_label', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('forum', ['Label'])

        # Adding model 'Answer'
        db.create_table('forum_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('forum', ['Answer'])

        # Adding M2M table for field points on 'Answer'
        db.create_table('forum_answer_points', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('answer', models.ForeignKey(orm['forum.answer'], null=False)),
            ('point', models.ForeignKey(orm['forum.point'], null=False))
        ))
        db.create_unique('forum_answer_points', ['answer_id', 'point_id'])

        # Adding model 'Question'
        db.create_table('forum_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('forum', ['Question'])

        # Adding M2M table for field labels on 'Question'
        db.create_table('forum_question_labels', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['forum.question'], null=False)),
            ('label', models.ForeignKey(orm['forum.label'], null=False))
        ))
        db.create_unique('forum_question_labels', ['question_id', 'label_id'])

        # Adding M2M table for field answers on 'Question'
        db.create_table('forum_question_answers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['forum.question'], null=False)),
            ('answer', models.ForeignKey(orm['forum.answer'], null=False))
        ))
        db.create_unique('forum_question_answers', ['question_id', 'answer_id'])

        # Adding M2M table for field points on 'Question'
        db.create_table('forum_question_points', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['forum.question'], null=False)),
            ('point', models.ForeignKey(orm['forum.point'], null=False))
        ))
        db.create_unique('forum_question_points', ['question_id', 'point_id'])

        # Deleting field 'ForumUser.points'
        db.delete_column('forum_forumuser', 'points')


    def backwards(self, orm):
        # Deleting model 'Point'
        db.delete_table('forum_point')

        # Deleting model 'Label'
        db.delete_table('forum_label')

        # Deleting model 'Answer'
        db.delete_table('forum_answer')

        # Removing M2M table for field points on 'Answer'
        db.delete_table('forum_answer_points')

        # Deleting model 'Question'
        db.delete_table('forum_question')

        # Removing M2M table for field labels on 'Question'
        db.delete_table('forum_question_labels')

        # Removing M2M table for field answers on 'Question'
        db.delete_table('forum_question_answers')

        # Removing M2M table for field points on 'Question'
        db.delete_table('forum_question_points')


        # User chose to not deal with backwards NULL issues for 'ForumUser.points'
        raise RuntimeError("Cannot reverse this migration. 'ForumUser.points' and its values cannot be restored.")

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
        'forum.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'apoint+'", 'symmetrical': 'False', 'to': "orm['forum.Point']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'forum.forumuser': {
            'Meta': {'object_name': 'ForumUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'forum.label': {
            'Meta': {'object_name': 'Label'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'forum.point': {
            'Meta': {'object_name': 'Point'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'fromuser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'forum.question': {
            'Meta': {'object_name': 'Question'},
            'answers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'answer+'", 'symmetrical': 'False', 'to': "orm['forum.Answer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labels': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lable+'", 'symmetrical': 'False', 'to': "orm['forum.Label']"}),
            'points': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'qpoint+'", 'symmetrical': 'False', 'to': "orm['forum.Point']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['forum']