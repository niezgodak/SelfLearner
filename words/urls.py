from django.urls import path, re_path
from .views import LanguagesView, WordGroupsView, WordsView, WordCreateView, AddWordGroupsView,\
    DeleteWordGroupsView, LearningView, WordsDataView, WordDataView

app_name = 'words'

urlpatterns = [
    path('languages/', LanguagesView.as_view(), name='languages'),
    re_path(r'^wordgroups/(?P<name>([A-Za-z])+)/wordsdata/$', WordsDataView.as_view(), name="wordsdata"),
    re_path(r'^wordgroups/wordsdata/(?P<pk>\d+)/$', WordDataView.as_view(), name="wordsdataupdate"),
    re_path(r'^wordgroups/(?P<num>\d+)/create$', AddWordGroupsView.as_view(), name="addwordgroups"),
    re_path(r'^wordgroups/(?P<num>\d+)/$', WordGroupsView.as_view(), name="wordgroups"),
    re_path(r'^deletegroup/(?P<pk>\d+)/$', DeleteWordGroupsView.as_view(), name="deletegroups"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z])+)/$', WordsView.as_view(), name="words"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z])+)/create/$', WordCreateView.as_view(), name="create"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z])+)/learn/$', LearningView.as_view(), name="learn"),

]