from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create_test' ,create_test, name="create_test"),
    path('add_test' ,add_test, name="add_test"),
    path('add', add_show , name='add_show'),
    path('show_all', show_questions , name='show_questions'),
]