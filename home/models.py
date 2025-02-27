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
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)  # Razorpay order ID
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)  # Razorpay payment ID

    def __str__(self):
        return f"{self.user.username} - {self.parking_space.title}"