from django import template
from forum.models import Question, Answer
register = template.Library()

@register.filter
def user_points(user):
    result = 0
    for question in Question.objects.filter(user__id__exact=user.id):
        result=+question.points.count()
    for answer in Answer.objects.filter(user__id__exact=user.id):
        result=+answer.points.count()
    return result

