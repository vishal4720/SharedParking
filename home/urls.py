from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('listing/',views.listing,name="listing"),
    path('booking/',views.booking,name="booking"),
    path('confirm-booking/',views.confirmBooking,name="confirm-booking"),
    path('dashboard/',views.dashboard,name="dashboard"),
]