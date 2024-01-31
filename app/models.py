from django.db import models
from django import forms
from django.core import validators

# Create your models here.
def validate_with_a(self):
    if self.lower().startswith('a'):
        raise forms.ValidationError('starts with a')



class Student(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True,validators=[validate_with_a])
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])


    def __str__(self):
        return self.Sname
