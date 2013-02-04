from forum.models import Question, Point, userPoint
from django.contrib.auth.models import User
from django.test import TestCase
import json


class SimpleTest(TestCase):

    fixtures = ['single']

    def test_basic_addition(self):
        user = User.objects.all()[0]
        point = Point()
        point.fromuser = user
        point.save()

        question = Question();
        question.user = user
        question.title = "hi"
        question.slug = 'something'
        question.text = 'else'
        question.save()
        question.points.add(point)
        question.save()
        
        self.assertEquals(1, question.total_points())

    def test_add_point_to_question(self):
        self.client.login(username='josh', password='asxdfv')
        user = User.objects.all()[0]

        question = Question();
        question.user = user
        question.title = "hi"
        question.slug = 'something'
        question.text = 'else'
        question.save()

        response = self.client.post('/ajax/forum/upvote_question.json', {'question_pk': question.pk})
        json_response = json.loads(response.content)
        self.assertTrue(json_response['success'])
        self.assertTrue(json_response['data']['delta'], 1)
        self.assertEquals(1, Question.objects.all().count())
        
        response = self.client.post('/ajax/forum/upvote_question.json', {'question_pk': question.pk})
        json_response = json.loads(response.content)
        self.assertTrue(json_response['success'])
        self.assertTrue(json_response['data']['delta'], -1)
        print Point.objects.all()
        self.assertEquals(0, Point.objects.all().count())

    def test_user_points(self):
        josh = User.objects.all()[0]

        question = Question();
        question.user = josh
        question.title = "hi"
        question.slug = 'something'
        question.text = 'else'
        question.save()

        point = Point()
        point.fromuser = josh
        point.save()
        question.points.add(point)

        user = User()
        user.save()
        point = Point()
        point.fromuser = user
        point.save()
        question.points.add(point)

        self.assertEquals(2, userPoint(josh))
