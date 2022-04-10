from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic.edit import FormView, CreateView

from . import forms
from words.models import Languages, WordGroup, Word
from django.views.generic.base import TemplateView

from django.shortcuts import render
from django.views import View

from .forms import WordForm


class LanguagesView(View):
    def get(self, request):
        languages = Languages.objects.all()
        ctx = {
            'languages': languages
        }
        return render(request, "words/languages.html", ctx)


class WordGroupsView(View):
    def get(self, request, num):
        word_groups = WordGroup.objects.filter(language=num)
        ctx = {
            'wordgroups': word_groups
        }
        return render(request, "words/wordgroups.html", ctx)

class AddWordGroupsView(View):
    def get(self, request, name):
        word_groups = WordGroup.objects.filter(language=num)
        ctx = {
            'wordgroups': word_groups
        }
        return render(request, "words/wordgroups.html", ctx)

class WordsView(View):
    def get(self, request, name):
        words = Word.objects.filter(wordgroup=WordGroup.objects.get(name=name))
        ctx = {
            'words': words
        }
        return render(request, "words/words.html", ctx)



class WordCreateView(View):
    def get(self, request, name):
        form = forms.WordForm()
        return render(request, 'words/word_form.html', {'form': form})
    def post(self, request, name):
        form = WordForm(request.POST)
        group = WordGroup.objects.get(name=name)
        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            group.words.add(word)
        return redirect('/home/')
