from django.db import models
from django import forms

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=2088)
"""
class Product(forms.Form):
    name = forms.CharField(max_length=255)
    price = forms.FloatField()
    category = forms.CharField(max_length=255)
    image = forms.CharField(max_length=2088)
"""