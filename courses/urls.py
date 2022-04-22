from django.urls import path, re_path
from .views import AddCourseView, YourCoursesView, CourseDetailsView, DeleteCourseView, EditCourseView,\
    CourseAddStudentsView, CreatePostView, FlashCardsView, AddFlashCardsView, AddFCView, DeleteFCView

app_name = 'courses'

urlpatterns = [
    re_path(r'^createcourse/$', AddCourseView.as_view(), name="createcourse"),
    re_path(r'^courses/$', YourCoursesView.as_view(), name="yourcourses"),
    re_path(r'^courses/(?P<user_pk>\d+)/(?P<name>([ A-Za-z0-9 _ ,!.@;()#$%^&*/><])+)/$', CourseDetailsView.as_view(),
            name="coursedetails"),
    re_path(r'^deletecourse/(?P<pk>\d+)/$', DeleteCourseView.as_view(), name="deletecourse"),
    re_path(r'^editcourse/(?P<pk>\d+)/$', EditCourseView.as_view(), name="editcourse"),
    re_path(r'^addstudents/(?P<pk>\d+)/$', CourseAddStudentsView.as_view(), name="addstudents"),
    re_path(r'^addpost/(?P<pk>\d+)/$', CreatePostView.as_view(), name="createpost"),
    re_path(r'^flashcards/(?P<pk>\d+)/$', FlashCardsView.as_view(), name="flashcards"),
    re_path(r'^flashcards/(?P<pk>\d+)/add/$', AddFlashCardsView.as_view(), name="addflashcards"),
    re_path(r'^addflashcard/(?P<course_name>([ A-Za-z0-9 _ ,!.@;()#$%^&*/><])+)/(?P<group_name>([ A-Za-z0-9 _ ,!.@;()#$%^&*/><])+)/(?P<user_pk>\d+)/$',
            AddFCView.as_view(), name="addflashcard"),
    re_path(r'^deleteflashcard/(?P<course_name>([ A-Za-z0-9 _ ,!.@;()#$%^&*/><])+)/(?P<group_name>([ A-Za-z0-9 _ ,!.@;()#$%^&*/><])+)/(?P<user_pk>\d+)/$',
            DeleteFCView.as_view(), name="addflashcard"),

]