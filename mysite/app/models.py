from django.db import models


class Book(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    guest=models.CharField(max_length=5)
    dob=models.CharField(max_length=15)
    time=models.CharField(max_length=10)
    message=models.TextField(max_length=80)

class signin(models.Model):
    uname=models.CharField(max_length=15)
    password=models.CharField(max_length=15)




