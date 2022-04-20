import pytest as pytest
from django.contrib.auth.models import Group
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, reverse_lazy
from words.models import Word, WordGroup, Languages
from words.forms import WordForm
import json


class TestForms(SimpleTestCase):
    def test_word_form_valid_data(self):
        form = WordForm(data={
        'your_language': 'Mleko',
        'foreign_language': 'Milk',
        'example_of_use': 'This is milk',
        'is_learned': False,
        'counter': 0})
        self.assertTrue(form.is_valid())

    def test_word_form_no_data(self):
        form = WordForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


