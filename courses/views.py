from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from . import forms
from words.models import WordGroup, Word
from users.models import Account
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CourseForm, CourseAddStudentsForm, PostForm
from .models import Course, Post


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
        return redirect(reverse('courses:yourcourses'))


class YourCoursesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request):
        courses = Course.objects.filter(students=Account.objects.get(pk=request.user.pk))
        ctx = {
            'courses': courses
        }
        return render(request, "courses/courses_overview.html", ctx)


class CourseDetailsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, user_pk, name):
        if request.user.is_teacher is True and Course.objects.get(name=name).owner == request.user:
            courses = Course.objects.filter(owner=user_pk)
            course = courses.get(name=name)
            posts = Post.objects.filter(course=course)
            students = course.students.all()
            ctx = {
                'course': course,
                'posts': posts,
                'students': students
                }
            return render(request, "courses/course_details_teacher.html", ctx)
        else:
            course = Course.objects.filter(students=Account.objects.get(pk=user_pk)).get(name=name)
            posts = Post.objects.filter(course=course)
            students = course.students.all()

            ctx = {
                'course': course,
                'posts': posts,
                'students': students
                }
            return render(request, "courses/course_details.html", ctx)


class DeleteCourseView(PermissionRequiredMixin, DeleteView):
    permission_required = 'courses.delete_course'
    login_url = reverse_lazy('users:login')
    model = Course
    success_url = reverse_lazy('courses:yourcourses')


class EditCourseView(PermissionRequiredMixin, UpdateView):
    permission_required = 'courses.change_course'
    model = Course
    fields = ['name', 'info']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('courses:yourcourses')


class CourseAddStudentsView(PermissionRequiredMixin, View):
    permission_required = 'courses.change_course'

    def get(self, request, pk):
        form = forms.CourseAddStudentsForm()
        return render(request, 'courses/course_add_students.html', {'form': form})

    def post(self, request, pk):
        form = CourseAddStudentsForm(request.POST)
        course = Course.objects.get(id=pk)
        if form.is_valid():
            student = form.data['students']
            course.students.add(student)
        return redirect(reverse('courses:yourcourses'))


class CreatePostView(PermissionRequiredMixin, View):
    permission_required = 'courses.change_course'

    def get(self, request, pk):
        form = forms.PostForm()
        return render(request, 'courses/course_post.html', {'form': form})

    def post(self, request, pk):
        form = PostForm(request.POST)
        course = Course.objects.get(id=pk)
        if form.is_valid():
            post = form.save(commit=False)
            post.course = course
            post.save()
        return redirect(reverse('courses:yourcourses'))


class FlashCardsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, pk):
        name = Course.objects.get(pk=pk).name
        course = Course.objects.get(pk=pk)
        owner = course.owner
        form = forms.CommentForm()
        word_groups = course.flashcards.all()
        ctx = {
            'wordgroups': word_groups,
            'user': request.user,
            'course': course,
            'owner': owner,
            'form': form
        }
        if request.user.is_teacher is True and \
                Course.objects.get(name=name).owner == request.user:
            return render(request, "courses/flashcards_teacher.html", ctx)
        else:
            return render(request, "courses/flashcards.html", ctx)


class AddFlashCardsView(PermissionRequiredMixin, View):
    permission_required = 'courses.change_course'

    def get(self, request, pk):
        word_groups = WordGroup.objects.filter(user=request.user)
        course = Course.objects.get(pk=pk)
        ctx = {
            'wordgroups': word_groups,
            'user': request.user,
            'course': course
        }
        return render(request, "courses/add_flashcards.html", ctx)


class AddFCView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, course_name, group_name, user_pk):
        wordgroup = WordGroup.objects.filter(name=group_name).get(user=user_pk)
        course = Course.objects.get(name=course_name)
        course.flashcards.add(wordgroup)
        return redirect(reverse('courses:flashcards', args=[course.pk]))


class DeleteFCView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, course_name, group_name, user_pk):
        wordgroup = WordGroup.objects.filter(name=group_name).get(user=user_pk)
        course = Course.objects.get(name=course_name)
        course.flashcards.remove(wordgroup)
        return redirect(reverse('courses:flashcards', args=[course.pk]))


class AddFlashcardGroupView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, course_pk, group_name, owner_pk, user_pk):
        wordgroup = WordGroup.objects.filter(name=group_name).get(user=owner_pk)
        words = Word.objects.filter(wordgroup=wordgroup)
        # language_number = wordgroup.language.id
        user = Account.objects.get(pk=user_pk)
        data = {
            'name': wordgroup.name,
            'language': wordgroup.language
        }
        new_group = WordGroup.objects.create(**data)
        new_group.user.add(user)
        for word in words:
            new_group.words.add(word)
        return redirect(reverse('courses:flashcards', args=[course_pk]))
