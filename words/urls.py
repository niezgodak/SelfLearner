from django.urls import path, re_path
from .views import LanguagesView, WordGroupsView, WordsView

app_name = 'words'

urlpatterns = [
    path('languages/', LanguagesView.as_view(), name='languages'),
    re_path(r'^wordgroups/(?P<num>\d+)/$', WordGroupsView.as_view(), name="wordgroups"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z])+)/$', WordsView.as_view(), name="words")

]