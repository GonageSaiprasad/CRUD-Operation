from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=70)
    username=models.CharField(max_length=70)
    password=models.CharField(max_length=10)
    confirmpassword=models.CharField(max_length=10)
    mob=models.IntegerField()
    gender=models.CharField(max_length=10)
    skill=models.CharField(max_length=10)

