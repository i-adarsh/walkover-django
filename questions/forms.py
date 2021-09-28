from django.core import validators
from django import forms
from .models import Questions


class add_question(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['questions', 'option1', 'option2', 'option3', 'option4', 'correct']
        widget = {
            'questions': forms.TextInput(attrs={'class': 'form-control'}),
            'option1': forms.TextInput(attrs={'class': 'form-control'}),
            'option2': forms.TextInput(attrs={'class': 'form-control'}),
            'option3': forms.TextInput(attrs={'class': 'form-control'}),
            'option4': forms.TextInput(attrs={'class': 'form-control'}),
            'correct': forms.TextInput(attrs={'class': 'form-control'}),
        }