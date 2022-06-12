from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Slotbooking(models.Model):

  token = models.CharField(unique=True,max_length=36,null=True)
  user = models.CharField(User,max_length=100,null=True,blank=True)
  name = models.CharField(max_length=122)
  email = models.EmailField(max_length=254)
  contact = models.CharField(max_length=50)
  # image= models.ImageField(null=True, blank=True)
  
  slots = models.CharField(max_length=50)
  date = models.DateField()

  def __str__(self):
      return self.user

  # def __str__(user):
  #     return user.name


