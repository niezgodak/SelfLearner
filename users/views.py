from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from words.models import Course
from . import forms
from django.contrib.auth import authenticate, login, logout


def login_user_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('home'))

    else:
        form = forms.LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('users:login'))


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            if user.is_teacher == True:
                p1 = Permission.objects.get(codename="add_course")
                p2 = Permission.objects.get(codename="change_course")
                p3 = Permission.objects.get(codename="delete_course")
                user.user_permissions.add(p1)
                user.user_permissions.add(p2)
                user.user_permissions.add(p3)
        return redirect(reverse_lazy('users:login'))
    return render(request, 'users/registration.html', {'form': form})
