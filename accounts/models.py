from django.db import models
from questions.models import Test
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz = models.ForeignKey(Test,on_delete=models.CASCADE)
    totalQuestions=models.IntegerField()
    correctAnswers=models.IntegerField()
    wrongAnswers=models.IntegerField()
    unattemptedQuestion=models.IntegerField()
    score = models.FloatField()
