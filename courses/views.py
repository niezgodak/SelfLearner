from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from . import forms
from words.models import Languages, WordGroup, Word
from users.models import Account
from django.shortcuts import render
from django.views import View
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from words.serializers import WordSerializer,\
    WordEditSerializer, WordGroupSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CourseForm, CourseEditForm
from .models import Course


class AddCourseView(PermissionRequiredMixin, View):
    permission_required = 'courses.add_course'
    def get(self, request):
        form = forms.CourseForm()
        return render(request, 'courses/course_form.html', {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)
        user = request.user
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = user
            course.save()
            course.students.add(user)
        return redirect(reverse('courses:yourcourses', args=[user.id]))

class YourCoursesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    def get(self, request, user_pk):
        courses = Course.objects.filter(students=Account.objects.get(pk=user_pk))
        ctx = {
            'courses': courses
        }
        return render(request, "courses/courses_overview.html", ctx)


class CourseDetailsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    def get(self, request, user_pk, name):
        courses = Course.objects.filter(students=Account.objects.get(pk=user_pk))
        course = courses.get(name=name)
        ctx = {
            'course': course
        }
        if request.user.is_teacher == True:
            return render(request, "courses/course_details_teacher.html", ctx)

        else:
            return render(request, "courses/course_details.html", ctx)


class DeleteCourseView(PermissionRequiredMixin, DeleteView):
    permission_required = 'courses.delete_course'
    login_url = reverse_lazy('users:login')
    model = Course
    success_url = reverse_lazy('courses:createcourse')

class EditCourseView(PermissionRequiredMixin, View):
    permission_required = 'courses.change_course'
    def get(self, request, course_pk):
        course = Course.objects.get(id=course_pk)
        ctx = {
        'form': forms.CourseEditForm(),
        'course': course
        }
        return render(request, 'courses/course_edit.html', ctx)
# TODO post in editig
    def post(self, request):
        form = CourseEditForm(request.POST)
        user = request.user
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = user
            course.save()
            course.students.add(user)
        return redirect(reverse('courses:yourcourses', args=[user.id]))
