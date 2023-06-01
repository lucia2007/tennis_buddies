from django.shortcuts import render, redirect
from datetime import datetime, timedelta
# from .models import *
from django.views.generic import CreateView
from django.contrib import messages
from .models import Booking, Court, Event
from .forms import BookingForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


def booking(request):
    return render(request, "bookings/booking.html", {})


class AddBooking(LoginRequiredMixin, CreateView):
    """" Add booking view """
    template_name = 'bookings/add.html'
    model = Booking
    form_class = BookingForm
    success_url = '/'

    # Updates the instance of the user to the current signed in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        # If form is valid, it leads to a reload.
        # It returns an object that represents the parent class.
        return super(AddBooking, self).form_valid(form)
