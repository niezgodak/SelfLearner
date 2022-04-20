import factory
from faker import Faker
fake = Faker()
from users.models import Account

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account
    name = fake.name()
    email = fake.email()
    is_teacher = 'False'

