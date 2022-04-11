from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse, reverse_lazy
from django.views.generic.edit import FormView, CreateView, DeleteView
from json import dumps
import json
from . import forms
from words.models import Languages, WordGroup, Word
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View
from .forms import WordForm, WordGroupForm


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
            'wordgroups': word_groups,
            'num': num
        }
        return render(request, "words/wordgroups.html", ctx)

class AddWordGroupsView(View):
    def get(self, request, num):
        form = forms.WordGroupForm()
        return render(request, 'words/wordgroup_form.html', {'form': form})
    def post(self, request, num):
        form = WordGroupForm(request.POST)
        language = Languages.objects.get(id=num)
        if form.is_valid():
            group = form.save(commit=False)
            group.language = language
            group.save()
        return redirect(reverse('words:wordgroups', args=[num]))

class DeleteWordGroupsView(DeleteView):
    model = WordGroup
    success_url = reverse_lazy('words:languages')

class WordsView(View):
    def get(self, request, name):
        words = Word.objects.filter(wordgroup=WordGroup.objects.get(name=name))
        ctx = {
            'words': words,
            'name': name
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
        return redirect(reverse('words:words', args=[name]))

class LearningView(View):
    def get(self, request, name):
        words = Word.objects.filter(wordgroup=WordGroup.objects.get(name=name))
        t = []
        for word in words:
            data = {
                'your_language': word.your_language,
                'foreign_language': word.foreign_language,
                'example_of_use': word.example_of_use,
                'is_learned': word.is_learned,
                'counter': word.counter
            }
            data_json = json.dumps(data)
            t.append(data)

        return render(request, "words/learning.html", {'words': words})