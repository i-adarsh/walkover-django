from django.shortcuts import render
from questions.models import *
from accounts.models import *
from random import shuffle
# Create your views here.
def test(request,token):
    quiz = Test.objects.get(link=token)
    allQues=list(quiz.allQuestions.all())
    shuffle(allQues)
    return render(request, "quiz.html", {"quiz": allQues,'time': quiz.time,'test':quiz})

def result(request):
    if request.method == 'POST':
        correctAnswers = 0
        wrongAnswers = 0
        test = Test.objects.get(id=int(request.POST.get('testId')))
        totalQuestions = len(test.allQuestions.all()) 
        for key,value in request.POST.items():
            try:
                ans = test.allQuestions.get(id=int(key)).correct
                if ans == value:
                    correctAnswers+=1
                else:
                    wrongAnswers+=1
            except:
                pass
        TakenQuiz.objects.create(
            user=request.user,
            quiz=test,
            totalQuestions=totalQuestions,
            correctAnswers=correctAnswers,
            wrongAnswers=wrongAnswers,
            unattemptedQuestion=int(totalQuestions-correctAnswers-wrongAnswers),
            score=correctAnswers/totalQuestions*100,
        )
        return render(request, 'result.html', {
            'totalQuestions': totalQuestions, 
            'correctAnswers': correctAnswers,
            'wrongAnswers':wrongAnswers,
            'unattemptedQuestion':int(totalQuestions-correctAnswers-wrongAnswers),
            'score':correctAnswers/totalQuestions*100,
        })