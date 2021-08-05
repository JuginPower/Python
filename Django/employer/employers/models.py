from django.db import models
from django.forms import forms

class Person(models.Model):

    username = models.CharField(max_length=20)
    