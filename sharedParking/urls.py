from django.contrib import admin
from django.urls import path,include
from home import views as homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")), 
]
