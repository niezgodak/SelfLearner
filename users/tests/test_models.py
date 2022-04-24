import pytest as pytest

@pytest.fixture(scope='function')
def user(db, django_user_model):
    user = django_user_model.objects.create_user(email='test@test.pl', name='testname', password='123')
    return user

def test_create_user(user, django_user_model):
    users = django_user_model.objects.all()
    assert len(users) == 1

def test_change_password(user):
    user.set_password('321')
    assert user.check_password('321') is True