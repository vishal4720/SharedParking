from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as userLogin,logout as userLogout
import razorpay
from .models import Booking
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def index(request):
    return render(request,"home/home.html")


def listing(request):
    return render(request,"home/listing_page.html")

@login_required(login_url="/login/")
def confirmBooking(request,spot):
    if request.method=="POST":
        # booking = Booking.objects.create()
        redirect('checkout ')
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


@login_required
def checkout(request, booking_id):
    print(booking_id)
    booking = get_object_or_404(Booking, id=booking_id)
    # Convert total price to paise (Razorpay uses paise for INR)
    amount = int(booking.total_price * 100)
    
    # Create a Razorpay order
    data = {
        "amount": amount,
        "currency": "INR",
        "receipt": f"order_rcptid_{booking.id}",
        "notes": {
            "booking_id": booking.id,
        }
    }
    order = client.order.create(data=data)
    
    # Save the Razorpay order ID to the booking
    booking.razorpay_order_id = order['id']
    booking.save()
    
    return render(request, "home/checkout.html", context= {
        'booking': booking,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'order_id': order['id'],
        'amount': amount,
    })

# from django.views.decorators.csrf import csrf_exempt

@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    # Get parameters from the URL
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    razorpay_signature = request.GET.get('razorpay_signature')
    
    # Verify the payment signature
    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': razorpay_payment_id,
        'razorpay_signature': razorpay_signature,
    }
    
    try:
        client.utility.verify_payment_signature(params_dict)
        booking.paid = True
        booking.razorpay_payment_id = razorpay_payment_id
        booking.save()
        return render(request, 'payment_success.html', {'booking': booking})
    except:
        return redirect('payment_failed')