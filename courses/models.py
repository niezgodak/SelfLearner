from django.db import models
from users.models import Account
from words.models import Word, WordGroup

class Course(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    word_group = models.ManyToManyField(WordGroup)
    owner = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="owner", null=True)
    students = models.ManyToManyField(Account)

class Post(models.Model):
    title = models.CharField(max_length=300)
    info = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
