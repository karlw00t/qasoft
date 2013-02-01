from django.forms import ModelForm
from forum.models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('user','points', 'answers')

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('user', 'points')
