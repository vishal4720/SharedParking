from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Parking Space
    path('parking/<int:id>/', views.parking_detail, name='parking_detail'),
    path('add-parking/', views.add_parking_space, name='add_parking_space'),

    # Booking
    path('booking/<int:id>/', views.booking_confirmation, name='booking_confirmation'),

    # Review
    path('review/<int:id>/', views.add_review, name='add_review'),

    # Profile
    path('profile/', views.profile, name='profile'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)