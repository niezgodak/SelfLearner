import pytest as pytest
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from words.models import Word, WordGroup, Languages
import json

@pytest.fixture(scope='function')
def user(db, django_user_model):
    Group.objects.create(name='learners')
    user = django_user_model.objects.create_user(email='test@test.pl', name='testname', password='123')
    return user

@pytest.fixture(scope='function')
def group(db):
    language = Languages.objects.create(language_name='testlanguage')
    group = WordGroup.objects.create(name='testgroup', language=language)
    return group


def test_languages_view_get(user):
    client = Client()
    client.force_login(user=user)
    response = client.get(reverse('words:languages'))
    assert response.status_code == 200

def test_wordgroups_view_get(user, group):
    client = Client()
    client.force_login(user=user)
    num = group.language.pk
    response = client.get(reverse('words:wordgroups', kwargs={'num': num}))
    assert response.status_code == 200


def test_addwordgroups_view_post(user):
    client = Client()
    client.force_login(user=user)
    user = user
    language = Languages.objects.create(language_name='testlanguage2')
    response = client.post(reverse('words:addwordgroups', kwargs={'num': language.pk}),
                           {'name': 'testgroup2',
                            'language': language})
    groups = WordGroup.objects.all()
    assert response.status_code == 302
    assert len(groups) == 1


