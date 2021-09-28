from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)

@admin.register(TakenQuiz)
class TakenQuizAdmin(admin.ModelAdmin):
    list_display=['user','quiz','score']
    list_filter = ['quiz']