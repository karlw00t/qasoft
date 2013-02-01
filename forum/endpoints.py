from ajax.exceptions import AJAXError
from forum.models import Question, Answer, Point
from django.http import HttpResponse


def upvote(request):
    question_pk = request.POST['question_pk']
    question = Question.objects.get(pk=question_pk)
    if (question.points.filter(fromuser__id__exact=request.user.id).count() != 0):
        response = HttpResponse("Could not upvote")
        response.status_code = 409
        return response
    point = Point()
    point.fromuser = request.user
    point.save()

    question.points.add(point)

    return {}
    
def downvote(request):
    return {}
