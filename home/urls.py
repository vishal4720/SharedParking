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

    # Payment URLs
    path('checkout/<int:booking_id>/', views.checkout, name='checkout'),
    path('payment-success/<int:booking_id>/', views.payment_success, name='payment_success'),
    # path('payment-failed/', views.payment_failed, name='payment_failed'),
]