from django.shortcuts import render, redirect
from datetime import datetime, timedelta
# from .models import *
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages
from .models import Booking, Court, Event
from .forms import BookingForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


def booking(request):
    return render(request, "bookings/booking.html", {})


class Bookings(ListView):
    """ Shows a list of all bookings """
    template_name = 'bookings/bookings.html'
    model = Booking
    context_object_name = 'bookings'


class BookingDetail(DetailView):
    """ View a single booking """
    template_name = 'bookings/detail.html'
    model = Booking
    context_object_name = 'booking'


class AddBooking(LoginRequiredMixin, CreateView):
    """" Add booking view """
    template_name = 'bookings/add.html'
    model = Booking
    form_class = BookingForm
    success_url = '/'

    # Updates the instance of the user to the current signed in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.booking = self.request.user.booking.owner
        # form.instance.user_profile = self.request.user.user_profile

        # If form is valid, it leads to a reload.
        # It returns an object that represents the parent class.
        return super(AddBooking, self).form_valid(form)
