from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ParkingSpace)
admin.site.register(models.Booking)
admin.site.register(models.Review)