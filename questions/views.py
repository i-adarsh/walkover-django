from django.shortcuts import render,HttpResponse
from .models import *
from .forms import add_question
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        question = add_question(request.POST)
        if question.is_valid():
            question.save()
            question = add_question()
            # question = question.cleaned_data['questions']
            # option1 = question.cleaned_data['option1']
            # option2 = question.cleaned_data['option2']
            # option3 = question.cleaned_data['option3']
            # option4 = question.cleaned_data['option4']
            # correct = question.cleaned_data['correct']
            # reg = Question(question, option1, option2, option3, option4, correct)
            # reg.save()
    else:
        question = add_question()
    return render(request, 'addandshow.html', {'form':question})

def show_questions(request):
    quest = Questions.objects.all()
    return render(request, 'showQuestions.html', {'question':quest})

def create_test(request):
    if request.user.is_authenticated:
        return render(request, 'create_test.html',{'questions':Questions.objects.all()})

def add_test(request):
    if request.method == 'POST':
        t=Test.objects.create(owner=request.user,name=request.POST['name'],time=request.POST['time'])
        for qid in request.POST.getlist('allQuestions'):
            t.allQuestions.add(Questions.objects.get(id=int(qid)))
        t.link = str(t.id).encode()
        t.save()
        return render(request, 'test_link.html', {'token': t.link,'name':t.name})
    else:
        return redirect('home')