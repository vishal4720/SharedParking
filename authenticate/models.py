from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    password = models.CharField(max_length=500,default="123456789")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
