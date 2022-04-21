import pytest as pytest
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from users.models import Account
import json

@pytest.fixture(scope='function')
def user(db, django_user_model):
    user = django_user_model.objects.create_user(email='test@test.pl', name='testname', password='123')
    return user

# def test_login_get(client):
#     url = reverse('users:login')
#     response = client.get(url)
#     assert response.status_code == 200
#
# def test_login_view_post(user):
#     client = Client()
#     response = client.post(reverse('users:login'),
#                            {'username': user.email,
#                             'password': user.password})
#     assert user.is_authenticated
