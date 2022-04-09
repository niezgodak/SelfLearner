from django.shortcuts import render, redirect
from django.urls.base import reverse

from words.models import Languages, WordGroup
from django.views.generic.base import TemplateView

from django.shortcuts import render
from django.views import View

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
