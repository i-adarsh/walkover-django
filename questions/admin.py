from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Questions)
class QuestionList(admin.ModelAdmin):
    list_display = ('id', 'questions', 'option1', 'option2','option3', 'option4', 'correct')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'time','link')