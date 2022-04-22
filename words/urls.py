from django.urls import path, re_path
from .views import LanguagesView, WordGroupsView, WordsView, WordCreateView, AddWordGroupsView,\
    DeleteWordGroupsView, DeleteWordView, LearningView, WordsDataView, WordDataView, ShareGroupView,\
    WordGroupDataView, AddCourseView, YourCoursesView

app_name = 'words'

urlpatterns = [
    path('languages/', LanguagesView.as_view(), name='languages'),
    re_path(r'^wordgroups/(?P<name>([A-Za-z0-9 _])+)/(?P<user_pk>\d+)/wordsdata/$', WordsDataView.as_view(), name="wordsdata"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z0-9 _])+)/wordgroupdata/$', WordGroupDataView.as_view(), name="wordgroupssdata"),
    re_path(r'^wordgroups/wordsdata/(?P<pk>\d+)/$', WordDataView.as_view(), name="wordsdataupdate"),
    re_path(r'^wordgroups/(?P<num>\d+)/create$', AddWordGroupsView.as_view(), name="addwordgroups"),
    re_path(r'^wordgroups/(?P<num>\d+)/$', WordGroupsView.as_view(), name="wordgroups"),
    re_path(r'^deletegroup/(?P<pk>\d+)/$', DeleteWordGroupsView.as_view(), name="deletegroups"),
    re_path(r'^deleteword/(?P<name>([A-Za-z0-9 _])+)/(?P<user_pk>\d+)/(?P<word_pk>\d+)/$', DeleteWordView.as_view(), name="deleteword"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z0-9 _])+)/(?P<user_pk>\d+)/$', WordsView.as_view(), name="words"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z0-9 _])+)/(?P<user_pk>\d+)/create/$', WordCreateView.as_view(), name="create"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z0-9 _])+)/(?P<user_pk>\d+)/learn/$', LearningView.as_view(), name="learn"),
    re_path(r'^wordgroups/(?P<name>([A-Za-z0-9 _])+)/(?P<user_pk>\d+)/share/$', ShareGroupView.as_view(), name="share"),
    re_path(r'^createcourse/$', AddCourseView.as_view(), name="createcourse"),
    re_path(r'^courses/(?P<user_pk>\d+)/$', YourCoursesView.as_view(), name="yourcourses"),

]