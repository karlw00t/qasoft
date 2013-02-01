from ajax.exceptions import AJAXError
from forum.models import Question, Answer, Point


def upvote(request):
    question_pk = request.POST['question_pk']
    question = Question.objects.get(pk=question_pk)
    point = Point()
    point.fromuser = request.user
    point.save()

    question.points.add(point)

    return {}
    
def downvote(request):
    return {}
