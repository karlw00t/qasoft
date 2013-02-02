# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forum.forms import QuestionForm, AnswerForm
from forum.models import Question
from django.shortcuts import get_object_or_404

def submit_question(request):
    if request.method == 'POST': 
        form = QuestionForm(request.POST)
        if form.is_valid(): 
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return HttpResponseRedirect('/question/' + question.slug) 
    else:
        form = QuestionForm() 

    return render(request, 'submit_question.html', {
        'form': form,
    })

def compare_question(left, right):
    return cmp(right.total_points(), left.total_points())

def list_question(request):
    questions = sorted(Question.objects.all(), compare_question)
    return render(request, 'list_question.html', {
        'questions':questions,
    })

def view_question(request,slug):
    question = get_object_or_404(Question, slug__exact=slug)
    if request.method == 'POST':
        form = AnswerForm(request.POST) 
        if form.is_valid(): 
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            question.answers.add(answer)
    form = AnswerForm()
    return render(request, 'view_question.html', {
        'question':question, 'form':form
    })
