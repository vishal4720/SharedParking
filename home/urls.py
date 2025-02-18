from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('listing/',views.listing,name="listing"),
    path('confirm-booking/<str:spot>',views.confirmBooking,name="confirm-booking"),
    path('dashboard/',views.dashboard,name="dashboard"),
]