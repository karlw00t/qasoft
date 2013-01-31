from forum.models import Question, Point
from django.contrib.auth.models import User
from django.test import TestCase


class SimpleTest(TestCase):

    fixtures = ['single']

    def test_basic_addition(self):
        user = User.objects.all()[0]
        point = Point()
        point.fromuser = user
        point.amount = 2
        point.save()

        question = Question();
        question.user = user
        question.title = "hi"
        question.slug = 'something'
        question.text = 'else'
        question.save()
        question.points.add(point)
        question.save()
        
        self.assertEquals(2, question.total_points())
