import pytest
from pytest_factoryboy import register
from django.contrib.auth.models import Group
from users.tests.factories import UserFactory

register(UserFactory)

@pytest.fixture
def user(db, user_factory):
    Group.objects.create(name='teachers')
    user = user_factory.create()
    return user