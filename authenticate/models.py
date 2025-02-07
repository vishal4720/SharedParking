from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
