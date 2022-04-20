import pytest as pytest
from django.contrib.auth.models import Group
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, reverse_lazy
from words.models import Word, WordGroup, Languages
from words.forms import WordForm, WordGroupForm
import json

@pytest.fixture(scope='function')
def user(db, django_user_model):
    Group.objects.create(name='teachers')
    user = django_user_model.objects.create_user(email='test@test.pl', name='testname', password='123')
    return user

@pytest.fixture(scope='function')
def language(db):
    language = Languages.objects.create(language_name="Spanish")
    return language

@pytest.fixture(scope='function')
def word(db):
    Group.objects.create(name='teachers')
    word = Word.objects.create(your_language='Mleko', foreign_language='Milk',
                               example_of_use='Test exmaple', is_learned=False,
                               counter=0)
    return word


# class TestWordForms(SimpleTestCase):
#     def test_word_form_valid_data(self):
#         form = WordForm(data={
#         'your_language': 'Mleko',
#         'foreign_language': 'Milk',
#         'example_of_use': 'This is milk',
#         'is_learned': False,
#         'counter': 0})
#         self.assertTrue(form.is_valid())
#
#     def test_word_form_no_data(self):
#         form = WordForm(data={})
#         self.assertFalse(form.is_valid())
#         self.assertEqual(len(form.errors), 2)
#
#     def test_word_form_only_necessary_data(self):
#         form = WordForm(data={'your_language': 'Mleko',
#         'foreign_language': 'Milk'})
#         self.assertTrue(form.is_valid())
#         self.assertEqual(len(form.errors), 0)

def test_word_group_form_valid_data(language):
    form = WordGroupForm(data={
        'name': 'Lesson',
        'language': language

     })
    assert form.is_valid()

def test_word_group_assign_many_to_many(language, user):
    wordgroup = WordGroup.objects.create(name='Lesson', language=language)
    wordgroup.user.add(user)
    groups = WordGroup.objects.all()
    assert len(groups) == 1




