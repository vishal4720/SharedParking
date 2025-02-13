from django.shortcuts import render,redirect
from django.urls import reverse
from .models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
def login(request):
    if request.method == "POST":
        req = request.POST
        user = User.objects.filter(email=req.get("your_email")).values()
        if check_password(req.get("your_pass"),user[0].get("password")):
            return redirect(reverse('home'))
    return render(request,'authenticate/login.html')


def signup(request):
    if request.method == "POST":
        req = request.POST
        user = User(name=req.get("name"),email=req.get("email"),age=req.get("age"),password=req.get("pass"))
        user.save()
    return render(request,'authenticate/signup.html')