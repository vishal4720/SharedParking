from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ParkingSpace, Booking, Review
from .forms import ParkingSpaceForm, BookingForm, ReviewForm

# Home Page
def home(request):
    parking_spaces = ParkingSpace.objects.filter(is_available=True)
    return render(request, 'home.html', {'parking_spaces': parking_spaces})


# Parking Space Detail
def parking_detail(request, id):
    parking_space = get_object_or_404(ParkingSpace, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.parking_space = parking_space
            # Calculate total price based on duration
            duration = (booking.end_time - booking.start_time).total_seconds() / 3600  # Duration in hours
            booking.total_price = float(parking_space.price_per_hour) * duration
            booking.save()
            return redirect('booking_confirmation', booking.id)
    else:
        form = BookingForm()
    return render(request, 'parking_detail.html', {'parking_space': parking_space, 'form': form})

# Booking Confirmation
def booking_confirmation(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'booking_confirmation.html', {'booking': booking})

# User Registration
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

# User Profile
@login_required
def profile(request):
    user_parking_spaces = ParkingSpace.objects.filter(host=request.user)
    return render(request, 'profile.html', {'user_parking_spaces': user_parking_spaces})

# Add Parking Space
@login_required
def add_parking_space(request):
    if request.method == 'POST':
        form = ParkingSpaceForm(request.POST, request.FILES)
        if form.is_valid():
            parking_space = form.save(commit=False)
            parking_space.host = request.user
            parking_space.save()
            return redirect('profile')
    else:
        form = ParkingSpaceForm()
    return render(request, 'add_parking_space.html', {'form': form})

# Add Review
@login_required
def add_review(request, id):
    parking_space = get_object_or_404(ParkingSpace, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.parking_space = parking_space
            review.save()
            return redirect('parking_detail', id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'parking_space': parking_space})
