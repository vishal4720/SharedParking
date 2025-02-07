from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'authenticate/login.html')


def signup(request):
    return render(request,'authenticate/signup.html')