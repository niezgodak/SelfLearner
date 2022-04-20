import pytest as pytest
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from words.models import Word, WordGroup, Languages
import json

