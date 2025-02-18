from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name="home"),
    path('listing/',views.listing,name="listing"),
    path('confirm-booking/<str:spot>',views.confirmBooking,name="confirm-booking"),
    path('dashboard/',views.dashboard,name="dashboard"),

    # Auth    
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
]