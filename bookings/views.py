from django.shortcuts import render, redirect
from datetime import datetime, timedelta
# from .models import *
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
    )
from django.contrib import messages
from .models import Booking, Court, Event
from .forms import BookingForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


def booking(request):
    return render(request, "bookings/booking.html", {})


class BookingListView(ListView):
    """ Shows a list of all bookings """
    template_name = 'bookings/list.html'
    model = Booking
    context_object_name = 'bookings'

    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-current-user
        """ 
        This view should return all the bookings when approached from
        Staff link (determined from the URL) or a filtered
        list of bookings approached from the profile/bookings
        """
        user = self.request.user.user_profile
        all_or_own = self.kwargs['all_or_own']
        if all_or_own == "all":
            return Booking.objects.all()
        else:
            return Booking.objects.filter(owner_id=user)


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


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit Booking """
    template_name = 'bookings/edit.html'
    model = Booking
    form_class = BookingForm
    success_url = '/bookings/list/all'

    def test_func(self):
        return self.request.user == self.get_object().owner.user

class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a booking """
    model = Booking
    success_url = '/bookings/list/all'

    def test_func(self):
        return self.request.user == self.get_object().owner.user
