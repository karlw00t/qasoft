from django.forms import ModelForm
from django import forms
from forum.models import Question, Answer

class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Your Question"

    class Meta:
        model = Question
        exclude = ('user','points', 'answers')

class AnswerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Your Answer"

    class Meta:
        model = Answer
        exclude = ('user', 'points')
        text =forms.DateField(label='Publication date')
