from django.db import models
from django.contrib.auth.models import User

import datetime
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

from django.db.models import Count

def userPoint(user):
    result = 0
    for question in Question.objects.filter(user__id__exact=user.id):
        result=+question.points.count()
    for answer in Answer.objects.filter(user__id__exact=user.id):
        result=+answer.points.count()
    return result


class Point(models.Model):
    fromuser = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, default=datetime.date.today())
    updated = models.DateTimeField(auto_now=True, default=datetime.date.today())

    def __unicode__(self):
        result = (str(self.fromuser))
        return result

class Answer(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    points = models.ManyToManyField(Point, related_name="apoint+")   
    created = models.DateTimeField(auto_now_add=True, default=datetime.date.today())
    updated = models.DateTimeField(auto_now=True, default=datetime.date.today())

    def __unicode__(self):
        return self.text

    def total_points(self):
        return self.points.all().count()

class Question(models.Model):
    user = models.ForeignKey(User)
    answers = models.ManyToManyField(Answer, related_name="answer+", blank=True, null=True)
    points = models.ManyToManyField(Point, related_name="qpoint+", blank=True, null=True)   
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', max_length=50, unique=True, help_text='Unique value for question page URL, created from title.')
    text = models.TextField()
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True, default=datetime.date.today())
    updated = models.DateTimeField(auto_now=True, default=datetime.date.today())

    def __unicode__(self):
        result = (self.slug, str(self.user))
        return ' - '.join(result)

    def total_points(self):
        return self.points.all().count()
