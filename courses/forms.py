from django import forms
from django.forms.models import ModelForm
from django.forms import Textarea
from .models import Course, Post, Comment
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

class CourseAddStudentsForm(ModelForm):
    class Meta:
        model = Course
        fields = ['students']
        # widgets = {
        #     'students': Textarea()
        # }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'info']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
