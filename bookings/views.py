from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
def booking(request):
    return render(request, "bookings/booking.html", {})


# Create your views here.
