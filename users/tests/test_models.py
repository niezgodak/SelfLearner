import pytest
from users.models import Account

def test_new_user(new_user):
    print(new_user.name)
    assert True