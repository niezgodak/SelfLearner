# import pytest as pytest
# from django.contrib.auth.models import Group
# from django.test import TestCase, Client
# from django.urls import reverse, reverse_lazy
# from users.models import Account
# import json
#
# @pytest.fixture(scope='function')
# def user(db, django_user_model):
#     user = django_user_model.objects.create_user(email='test@test.pl', name='testname', password='123')
#     return user
#
# def test_login_get(client):
#     """Testing response status code"""
#     url = reverse('users:login')
#     response = client.get(url)
#     assert response.status_code == 200
#
# def test_login_view_post(user):
#     """Testing login view with correct data"""
#     client = Client()
#     response = client.post(reverse('users:login'),
#                            {'username': user.email,
#                             'password': user.password})
#     assert user.is_authenticated
#
# def test_register_view_post(db, django_user_model):
#     """Testing registration with correct data"""
#     client = Client()
#     response = client.post(reverse('users:registration'),
#                            {'name': "Anna",
#                             'password': "123",
#                             'password2': "123",
#                             'email': "m@test.pl"
#                             })
#     users = django_user_model.objects.all()
#     assert len(users) == 1
#
# def test_register_view_incorrect_post(db, django_user_model):
#     """testing registration with not matching passwords"""
#     client = Client()
#     response = client.post(reverse('users:registration'),
#                            {'name': "Anna",
#                             'password': "123",
#                             'password2': "12",
#                             'email': "m@test.pl"
#                             })
#     users = django_user_model.objects.all()
#     assert len(users) == 0
#
# def test_register_view_incorrect_email_post(db, django_user_model):
#     """testing registration with incorrect email"""
#     client = Client()
#     response = client.post(reverse('users:registration'),
#                            {'name': "Anna",
#                             'password': "123",
#                             'password2': "123",
#                             'email': "mtest.pl"
#                             })
#     users = django_user_model.objects.all()
#     assert len(users) == 0
