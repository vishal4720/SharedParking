from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "title" : "Shared Parking Space",
        "total" : ["Meow","Kanchu","Vishal"],
        "user" : {
            "email":"vishalpatole2000@gmail.com",
            "name" : "Vishal Patole",    
        },
    }
    return render(request,"home/index.html",context=data)