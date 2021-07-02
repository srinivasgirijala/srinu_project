from django.db import models


# Create your models here.

class Newuser(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)

class Appli(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)
    email=models.EmailField()
    state=models.CharField(max_length=100) 
    address=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100) 
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=100) 
    textarea=models.CharField(max_length=100)