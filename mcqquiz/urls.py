from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<token>/', test , name='test'),
    path('result', result , name='result'),
]