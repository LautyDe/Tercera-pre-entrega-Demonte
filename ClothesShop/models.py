from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Shoe(models.Model):
  model = models.CharField(max_length=100)
  size = models.IntegerField(max_length=2)
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('name','size')
  
class Shirt(models.Model):
  model = models.CharField(max_length=100)
  size = models.IntegerField(max_length=2)
  def __str__(self):
    return f'{self.model} - {self.size}'
  class Meta():
    ordering = ('name','size')

class User(models.Model):
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()
  def __str__(self):
    return f'{self.name} {self.last_name}'