from django.db import models

# Create your models here.
class Register(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Gmail=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)