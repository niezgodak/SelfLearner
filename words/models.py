from django.db import models

# Create your models here.

class Languages(models.Model):
    language_name = models.CharField(max_length=100)

class Word(models.Model):
    your_language = models.CharField(max_length=100)
    foreign_language = models.CharField(max_length=100)
    example_of_use = models.TextField(null=True)
    is_learned = models.BooleanField(default=False)
    #user = add user models realation -> user from session? ForeignKey
    #language -> I don't know yet if it is needed

class WordGroup(models.Model):
    name = models.CharField(max_length=100)
    words = models.ManyToManyField("Word")
    language = models.ForeignKey("Languages", on_delete=models.PROTECT, null=True)


