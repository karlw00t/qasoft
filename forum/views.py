# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forum.forms import QuestionForm, AnswerForm
from forum.models import Question
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required
def submit_question(request):
    if request.method == 'POST': 
        form = QuestionForm(request.POST)
        if form.is_valid(): 
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            for tag in form.cleaned_data['tags']:
                question.tags.add(tag)
            question.save()
            return HttpResponseRedirect(reverse('forum.views.view_question', kwargs={'slug':question.slug}))
    else:
        form = QuestionForm() 

    return render(request, 'submit_question.html', {
        'form': form,
    })

def compare_question(left, right):
    return cmp(right.total_points(), left.total_points())

@login_required
def list_question(request):
    questions = sorted(Question.objects.all(), compare_question)
    return render(request, 'list_question.html', {
        'questions':questions,
    })

@login_required
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
