from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)

class Flight(models.Model):
    From1= models.CharField(max_length=50)
    to = models.CharField(max_length=50)
    price = models.IntegerField()