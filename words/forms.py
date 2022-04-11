from django import forms
from django.forms.models import ModelForm

from .models import Word, WordGroup
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['your_language', 'foreign_language', 'example_of_use']

class WordGroupForm(ModelForm):
    class Meta:
        model = WordGroup
        fields = ['name']
