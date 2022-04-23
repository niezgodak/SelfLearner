import pytest as pytest
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from pytest_django.asserts import assertTemplateUsed
from users.models import Account
from django.contrib.auth.models import Permission
from words.models import Word, WordGroup, Languages
from courses.models import Course, Post
from users.models import Account
import json

@pytest.fixture(scope='function')
def user(db, django_user_model):
    user = django_user_model.objects.create_user(email='test@test.pl', name='testname', password='123')
    return user

@pytest.fixture(scope='function')
def user2(db):
    user = Account.objects.create(email='test2@test2.pl', name='testname2', password='123', is_teacher="True")
    return user2

@pytest.fixture(scope='function')
def group(db):
    language = Languages.objects.create(language_name='testlanguage')
    group = WordGroup.objects.create(name='testgroup', language=language)
    return group

@pytest.fixture(scope='function')
def word(db):
    Group.objects.create(name='teachers')
    word = Word.objects.create(your_language='Mleko', foreign_language='Milk',
                               example_of_use='Test exmaple', is_learned=False,
                               counter=0)
    return word

@pytest.fixture(scope='function')
def course(db):
    course = Course.objects.create(name="Test course", info="Test information about course")
    return course




# def test_yourcourses_view_get(user):
#     '''Testing response status code'''
#     client = Client()
#     client.force_login(user=user)
#     response = client.get(reverse('courses:yourcourses'))
#     assert response.status_code == 200
#
# def test_yourcourses_view_get(user, course):
#     '''Testing adding course owner and displaying owner's courses '''
#     client = Client()
#     client.force_login(user=user)
#     course.owner = user
#     course.save()
#     courses = Course.objects.filter(owner=user)
#     response = client.get(reverse('courses:yourcourses'))
#     assert len(courses) == 1

# def test_creating_course_view_get(user):
#     '''Testing if it is possible to create course when you don't have permissions '''
#     client = Client()
#     client.force_login(user=user)
#     response = client.get(reverse('courses:createcourse'))
#     assert response.status_code == 403
#
# def test_creating_course_teacher_view_get(user):
#     '''Testing if it is possible to create course when you have permissions '''
#     user.is_teacher = True
#     p1 = Permission.objects.get(codename="add_course")
#     user.user_permissions.add(p1)
#     client = Client()
#     client.force_login(user=user)
#     response = client.get(reverse('courses:createcourse'))
#     assert response.status_code == 200

# def test_deleting_course_view(user, course):
#     '''Testing if it is possible to create course when you don't have permissions '''
#     client = Client()
#     client.force_login(user=user)
#     response = client.get(reverse('courses:deletecourse', kwargs={'pk': course.id}))
#     assert response.status_code == 403
#
# def test_deleting_course_teacher_view(user, course):
#     '''Testing if it is possible to create course when you have permissions '''
#     user.is_teacher = True
#     p1 = Permission.objects.get(codename="delete_course")
#     user.user_permissions.add(p1)
#     client = Client()
#     client.force_login(user=user)
#     response = client.get(reverse('courses:deletecourse', kwargs={'pk': course.id}))
#     assert response.status_code == 200

# def test_editing_course_view(user, course):
#     """Testing if it is possible to create course when you don't have permissions """
#     client = Client()
#     client.force_login(user=user)
#     response = client.get(reverse('courses:editcourse', kwargs={'pk': course.id}))
#     assert response.status_code == 403
#
# def test_editing_course_teacher_view(user, course):
#     """Testing if it is possible to create course when you have permissions """
#     user.is_teacher = True
#     p1 = Permission.objects.get(codename="change_course")
#     user.user_permissions.add(p1)
#     client = Client()
#     client.force_login(user=user)
#     response = client.get(reverse('courses:editcourse', kwargs={'pk': course.id}))
#     assert response.status_code == 200

