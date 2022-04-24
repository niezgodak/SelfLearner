import pytest as pytest
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from pytest_django.asserts import assertTemplateUsed
from users.models import Account
from words.models import Word, WordGroup, Languages
import json

@pytest.fixture(scope='function')
def user(db, django_user_model):
    user = django_user_model.objects.create_user(email='test@test.pl', name='testname', password='123')
    return user

@pytest.fixture(scope='function')
def user2(db, django_user_model):
    user = django_user_model.objects.create_user(email='test2@test2.pl', name='testname2', password='123')
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


def test_languages_view_get(user):
    """Testing view's status code"""
    client = Client()
    client.force_login(user=user)
    response = client.get(reverse('words:languages'))
    assert response.status_code == 200


def test_wordgroups_view_get(user, group):
    """Testting view's statuds code"""
    client = Client()
    client.force_login(user=user)
    num = group.language.pk
    response = client.get(reverse('words:wordgroups', kwargs={'num': num}))
    assert response.status_code == 200

def test_addwordgroups_view_post(user):
    """Testing adding new group"""
    client = Client()
    client.force_login(user=user)
    language = Languages.objects.create(language_name='testlanguage2')
    response = client.post(reverse('words:addwordgroups', kwargs={'num': language.pk}),
                           {'name': 'testgroup2',
                            'language': language})
    groups = WordGroup.objects.all()
    assert response.status_code == 302
    assert len(groups) == 1

def test_addwordgroups_view_post_nodata(user):
    """Testing adding new group with invalid data"""
    client = Client()
    client.force_login(user=user)
    language = Languages.objects.create(language_name='testlanguage2')
    response = client.post(reverse('words:addwordgroups', kwargs={'num': language.pk}), {})
    groups = WordGroup.objects.all()
    assert response.status_code == 302
    assert len(groups) == 0

def test_addwordgroups_view_post_incorrectdata(user):
    """Testing adding new group with invalid data"""
    client = Client()
    client.force_login(user=user)
    language = Languages.objects.create(language_name='testlanguage2')
    response = client.post(reverse('words:addwordgroups', kwargs={'num': language.pk}), {'name': ''})
    groups = WordGroup.objects.all()
    assert response.status_code == 302
    assert len(groups) == 0


def test_delete_wordgroup_view_post(group, user):
    """Testing deleting group"""

    client = Client()
    client.force_login(user=user)
    language = Languages.objects.create(language_name='testlanguage2')
    response = client.post(reverse('words:deletegroups', kwargs={'pk': group.pk}))
    groups = WordGroup.objects.all()
    assert len(groups) == 0

def test_delete_word_view(group, user, word):
    """Testing deleting word"""
    client = Client()
    client.force_login(user=user)
    group.words.add(word)
    group.user.add(user)
    print(group.words.all())
    response = client.get(reverse('words:deleteword', kwargs={'name': group.name,
                                                               'user_pk': user.id,
                                                               'word_pk': word.id}))
    words = group.words.all()
    assert len(words) == 0

def test_word_create_get(user, group):
    """Testing WordCreateView's template used"""

    client = Client()
    client.force_login(user=user)
    group.user.add(user)
    response = client.get(reverse('words:create', kwargs={'name': group.name,
                                                              'user_pk': user.id}))
    assert response.status_code == 200
    assertTemplateUsed(response, 'words/word_form.html')

def test_word_create_post(user, group):
    """Testing WordCreateView's - creating new word"""
    client = Client()
    client.force_login(user=user)
    group.user.add(user)
    response = client.post(reverse('words:create', kwargs={'name': group.name,
                                                              'user_pk': user.id}), {'your_language': 'test',
                                                                                     'foreign_language': 'test2'})
    words = Word.objects.all()
    assert response.status_code == 302
    assert len(words) == 1

def test_word_create_post_nodata(user, group):
    """Testing WordCreateView's - creating new word with no data"""

    client = Client()
    client.force_login(user=user)
    group.user.add(user)
    response = client.post(reverse('words:create', kwargs={'name': group.name,
                                                              'user_pk': user.id}), {})
    words = Word.objects.all()
    assert response.status_code == 302
    assert len(words) == 0

def test_word_create_post_incorrectdata(user, group):
    """Testing WordCreateView's - creating new word with incomplete data"""
    client = Client()
    client.force_login(user=user)
    group.user.add(user)
    response = client.post(reverse('words:create', kwargs={'name': group.name,
                                                              'user_pk': user.id}), {'your_language': 'Test'})
    words = Word.objects.all()
    assert response.status_code == 302
    assert len(words) == 0


def test_learning_view(user, group):
    """Testing LearningView's template used and response status code"""
    client = Client()
    client.force_login(user=user)
    group.user.add(user)
    response = client.get(reverse('words:learn', kwargs={'name': group.name,
                                                              'user_pk': user.id}))
    assert response.status_code == 200
    assertTemplateUsed(response, 'words/learning.html')


def test_share_group_share(user, group):
    """Testing SharingView's template used and response status code"""
    client = Client()
    client.force_login(user=user)
    group.user.add(user)
    response = client.get(reverse('words:share', kwargs={'name': group.name,
                                                              'user_pk': user.id}))
    assert response.status_code == 200
    assertTemplateUsed(response, 'words/wordgroup_share.html')

def test_word_api_get(word):
    """Testing WordAPIView's template used and response status code"""
    client = Client()
    response = client.get(reverse('words:wordsdataupdate', kwargs={'pk': word.id}))
    assert response.status_code == 200

