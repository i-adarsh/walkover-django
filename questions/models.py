from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    questions = models.TextField(max_length=250)
    option1 = models.TextField(max_length=100)
    option2 = models.TextField(max_length=100)
    option3 = models.TextField(max_length=100)
    option4 = models.TextField(max_length=100)
    correct = models.TextField(max_length=100)

    def __str__(self):
        return self.questions
    
class Test(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField()
    time = models.IntegerField()
    allQuestions = models.ManyToManyField(Questions,related_name="question")
    link= models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name