from django import forms
from django.forms.models import ModelForm
from .models import Course
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'info']


class CourseEditForm(ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'info']
