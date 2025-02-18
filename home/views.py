from django.shortcuts import render
from authenticate.models import User

# Create your views here.
def index(request):
    user = User.objects.all()
    return render(request,"home/home.html",context={"user":user})


def listing(request):
    return render(request,"home/listing_page.html")


def confirmBooking(request,spot):
    return render(request,"home/confirm_booking.html",{"spot":spot})


def dashboard(request):
    return render(request,"home/dashboard.html")