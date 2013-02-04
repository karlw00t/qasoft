from ajax.exceptions import AJAXError
from forum.models import Question, Answer, Point
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def upvote_question(request):
    question_pk = request.POST['question_pk']
    question = get_object_or_404(Question, pk=question_pk)
    points = question.points.filter(fromuser__id__exact=request.user.id)
    if (points.count() == 1):
        points.delete()
        return {'delta':-1}
    point = Point()
    point.fromuser = request.user
    point.save()
    question.points.add(point)
    return {'delta':1}

def upvote_answer(request):
    answer_pk = request.POST['answer_pk']
    answer = get_object_or_404(Answer, pk=answer_pk)
    points = answer.points.filter(fromuser__id__exact=request.user.id)
    if (points.count() == 1):
        points.delete()
        return {'delta':-1}
    point = Point()
    point.fromuser = request.user
    point.save()
    answer.points.add(point)
    return {'delta':1}

def delete_answer(request):
    answer_pk = request.POST['answer_pk']
    answer = get_object_or_404(Answer, pk=answer_pk)
    answer.delete()
