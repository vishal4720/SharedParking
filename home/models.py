from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ParkingSpace(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='parking_images/')
    video = models.FileField(upload_to='parking_videos/', null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title