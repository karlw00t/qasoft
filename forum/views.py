# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forum.forms import QuestionForm
from forum.models import Question

def submit_question(request):
    if request.method == 'POST': # If the form has been submitted...
        form = QuestionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return HttpResponseRedirect('/question/' + question.slug) # Redirect after POST
    else:
        form = QuestionForm() # An unbound form

    return render(request, 'submit_question.html', {
        'form': form,
    })

def view_question(request,slug):
    question = Question.objects.get(slug__exact=slug)
    print question.title
    return render(request, 'view_question.html', {
        'question':question,
    })

def upvote(request, question_pk):
    pass

