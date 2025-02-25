from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as userLogin,logout as userLogout

# Create your views here.
def index(request):
    return render(request,"home/home.html")


def listing(request):
    return render(request,"home/listing_page.html")

@login_required(login_url="/login/")
def confirmBooking(request,spot):
    return render(request,"home/confirm_booking.html",{"spot":spot})


@login_required
def dashboard(request):
    return render(request,"home/dashboard.html")


def login(request):
    if request.method == "POST":
        req = request.POST
        user = authenticate(username=req.get("your_email"), password=req.get("your_pass"))
        if user is not None:
            userLogin(request,user)
            if request.method == "GET":
                next=request.GET.get("next")
                if next is not None:
                    print(next)
            return redirect('home',permanent=True)
        

 
    return render(request,'login.html')


def signup(request):
    if request.method == "POST":
        req = request.POST
        user = User.objects.create_user(email=req.get("email"),username=req.get("email"),password=req.get("pass"))
        user.save()
        userLogin(request,user)
        return redirect('home',permanent=True)
    return render(request,'signup.html')


@login_required
def logout(request):
    userLogout(request)
    return redirect('home',permanent=True)