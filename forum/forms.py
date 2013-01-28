from django.forms import ModelForm
from forum.models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('user','points', 'answers')
