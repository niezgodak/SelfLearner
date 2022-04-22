from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from . import forms
from words.models import Languages, WordGroup, Word, Course
from users.models import Account
from django.shortcuts import render
from django.views import View
from .forms import WordForm, WordGroupForm, CourseForm
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from words.serializers import WordSerializer,\
    WordEditSerializer, WordGroupSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class LanguagesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request):
        languages = Languages.objects.all()
        ctx = {
            'languages': languages
        }
        return render(request, "words/languages.html", ctx)


class WordGroupsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, num):
        word_groups = WordGroup.objects.filter(language=num).filter(user=request.user)
        ctx = {
            'wordgroups': word_groups,
            'num': num,
            'user': request.user
        }
        return render(request, "words/wordgroups.html", ctx)


class AddWordGroupsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, num):
        form = forms.WordGroupForm()
        return render(request, 'words/wordgroup_form.html', {'form': form})

    def post(self, request, num):
        form = WordGroupForm(request.POST)
        language = Languages.objects.get(id=num)
        user = request.user
        if form.is_valid():
            group = form.save(commit=False)
            group.language = language
            group.save()
            group.user.add(user)
        return redirect(reverse('words:wordgroups', args=[num]))


class DeleteWordGroupsView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = WordGroup
    success_url = reverse_lazy('words:languages')


class DeleteWordView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, name, user_pk, word_pk):
        wordgroup = WordGroup.objects.filter(name=name).get(user=user_pk)
        word = Word.objects.get(pk=word_pk)
        wordgroup.words.remove(word)
        return redirect(reverse('words:words', args=[name, user_pk]))


class WordsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, name, user_pk):
        user = request.user
        wordgroup = WordGroup.objects.filter(name=name).get(user=user_pk)
        words = Word.objects.filter(wordgroup=wordgroup)
        ctx = {
            'words': words,
            'name': name,
            'user': user
        }
        return render(request, "words/words2.html", ctx)


class WordCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, name, user_pk):
        form = forms.WordForm()
        return render(request, 'words/word_form.html', {'form': form})

    def post(self, request, name, user_pk):
        form = WordForm(request.POST)
        group = WordGroup.objects.filter(name=name).get(user=user_pk)
        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            group.words.add(word)
        return redirect(reverse('words:words', args=[name, user_pk]))


class WordsDataView(APIView):
    def get(self, request, name, user_pk):
        wordgroup = WordGroup.objects.filter(name=name).get(user=user_pk)
        words = Word.objects.filter(wordgroup=wordgroup)
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)


class WordDataView(APIView):
    def get_object(self, pk):
        try:
            return Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        word = self.get_object(pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def put(self, request, pk):
        word = self.get_object(pk)
        serializer = WordEditSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LearningView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, name, user_pk):
        wordgroup = WordGroup.objects.filter(name=name).get(user=user_pk)
        words = Word.objects.filter(wordgroup=wordgroup)
        language = wordgroup.language
        lan_id = language.id
        ctx = {
            'words': words,
            'name': name,
            'lan_id': lan_id,
            'user': request.user
        }
        return render(request, "words/learning.html", ctx)


class ShareGroupView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, name, user_pk):
        user = request.user
        if int(request.user.id) == int(user_pk):
            wordgroup = WordGroup.objects.filter(name=name).get(user=user_pk)
            words = Word.objects.filter(wordgroup=wordgroup)
            ctx = {
                'words': words,
                'name': name,
                'user': user
            }
            return render(request, "words/wordgroup_share.html", ctx)
        else:
            wordgroup = WordGroup.objects.filter(name=name).get(user=user_pk)
            words = Word.objects.filter(wordgroup=wordgroup)
            ctx = {
                'words': words,
                'name': name,
                'user': user,
                'pk': user_pk
            }
            return render(request, "words/wordgroup_accept.html", ctx)

    def post(self, request, name, user_pk):
        if int(request.user.id) != int(user_pk):
            wordgroup = WordGroup.objects.filter(name=name).get(user=user_pk)
            words = Word.objects.filter(wordgroup=wordgroup)
            language_number = wordgroup.language.id
            user = request.user
            data = {
                'name': wordgroup.name,
                'language': wordgroup.language
            }
            new_group = WordGroup.objects.create(**data)
            new_group.user.add(user)
            for word in words:
                new_group.words.add(word)

            return redirect(reverse('words:wordgroups',
                                    kwargs={'num': language_number}))


class WordGroupDataView(APIView):
    def put(self, request, name):
        group = WordGroup.objects.get(name=name)
        serializer = WordGroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddCourseView(PermissionRequiredMixin, View):
    permission_required = 'words.add_course'
    def get(self, request):
        form = forms.CourseForm()
        return render(request, 'words/course_form.html', {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)
        user = request.user
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = user
            course.save()
            course.students.add(user)
        return redirect(reverse('words:yourcourses', args=[user.id]))

class YourCoursesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    def get(self, request, user_pk):
        courses = Course.objects.filter(students=Account.objects.get(pk=user_pk))
        ctx = {
            'courses': courses
        }
        return render(request, "words/courses_overview.html", ctx)


class CourseDetailsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    def get(self, request, user_pk, name):
        courses = Course.objects.filter(students=Account.objects.get(pk=user_pk))
        course = courses.get(name=name)
        ctx = {
            'course': course
        }
        if request.user.is_teacher == True:
            return render(request, "words/course_details_teacher.html", ctx)

        else:
            return render(request, "words/course_details.html", ctx)


class DeleteCourseView(PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = WordGroup
    success_url = reverse_lazy('words:languages')