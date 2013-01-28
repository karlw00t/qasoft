from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# Create your models here.

class Label(models.Model):
    text = models.CharField(max_length=15)

    def __unicode__(self):
        return self.text

class Point(models.Model):
    amount = models.IntegerField()
    fromuser = models.ForeignKey(User)

    def __unicode__(self):
        result = (str(self.amount), str(self.fromuser))
        return ' - '.join(result)

class Answer(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    points = models.ManyToManyField(Point, related_name="apoint+")   

    def __unicode__(self):
        return self.text
    

class Question(models.Model):
    user = models.ForeignKey(User)
    answers = models.ManyToManyField(Answer, related_name="answer+", blank=True, null=True)
    points = models.ManyToManyField(Point, related_name="qpoint+", blank=True, null=True)   
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', max_length=50, unique=True, help_text='Unique value for question page URL, created from title.')
    text = models.TextField()
    labels = models.ManyToManyField(Label, related_name="lable+")   

    def __unicode__(self):
        result = (self.slug, str(self.user))
        return ' - '.join(result)

    def total_points(self):
        return 1
