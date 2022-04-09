from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, PermissionsMixin
from django.db import models

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, name, last_name, password=None):
        if not email:
            raise ValueError("E-mail must be provided")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            last_name=last_name
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        if user.is_learner:
            learners_group = Group.objects.get(name='learners')
            user.groups.add(learners_group)
        return user

    def create_superuser(self, email, name, last_name, password=None):
        user = self.create_user(
            email=email, name=name, last_name=last_name, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, verbose_name='Email')
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_join = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomAccountManager()

    def __str__(self):
        return self.email
