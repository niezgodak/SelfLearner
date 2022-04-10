from django.db import models
from users.models import Account

# Create your models here.

class Languages(models.Model):
    language_name = models.CharField(max_length=100)

class Word(models.Model):
    your_language = models.CharField(max_length=100)
    foreign_language = models.CharField(max_length=100)
    example_of_use = models.TextField(null=True, blank=True)
    is_learned = models.BooleanField(default=False)
    user = models.ManyToManyField(Account)
    #user = add user models realation -> user from session? ManyToMany
    #language -> I don't know yet if it is needed
    counter = models.IntegerField(default=0)

class WordGroup(models.Model):
    name = models.CharField(max_length=100)
    words = models.ManyToManyField("Word")
    language = models.ForeignKey("Languages", on_delete=models.PROTECT, null=True)


