from django.db import models
from users.models import Account
from words.models import Word, WordGroup

class Course(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    word_group = models.ManyToManyField(WordGroup)
    owner = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="owner", null=True)
    students = models.ManyToManyField(Account)
    flashcards = models.ManyToManyField(WordGroup, related_name="flashcards")

class Post(models.Model):
    title = models.CharField(max_length=300)
    info = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="comment_owner", null=True)
    content = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post", null=True)


