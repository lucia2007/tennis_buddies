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
# to display messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Booking, Court, Event
from .forms import BookingForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# CRUD functionality was done following Dee Mc's Recipe tutorial: 
# https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy

def booking(request):
    return render(request, "bookings/booking.html", {})


class BookingListView(LoginRequiredMixin, ListView):
    """ Shows a list of all bookings """
    template_name = 'bookings/list.html'
    model = Booking
    context_object_name = 'bookings'

    def get_queryset(self):
        # https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-current-user
        """
        This view should return all the bookings when approached from
        Staff link (determined from the URL 'all') or a filtered
        list of bookings approached from the profile/bookings ('own')
        """
        all_or_own = self.kwargs['all_or_own']
        if all_or_own == "all":
            return Booking.objects.all()
        else:
            user = self.request.user.user_profile
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
    success_url = '/bookings/list/own'

    # Updates the instance of the user to the current signed in user
    # https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.owner = self.request.user.user_profile

        # Check if the booking is not in the past
        # https://stackoverflow.com/questions/73260028/how-can-i-check-if-date-is-passed-from-django-model
        booking_date = form.cleaned_data.get('date')
        if booking_date is not None and booking_date < timezone.now().date():
            messages.warning(self.request, f"You are trying to make a booking in the past. Change the date please.")

            return redirect('add-booking')

        # If form is valid, it leads to a reload.
        # It returns an object that represents the parent class.
        messages.success(self.request, f"Booking was created successfully.")
        return super(AddBooking, self).form_valid(form)


class EditBooking(
        LoginRequiredMixin,
        UserPassesTestMixin,
        SuccessMessageMixin,
        UpdateView):
    """ Edit Booking """
    template_name = 'bookings/edit.html'
    model = Booking
    form_class = BookingForm
    success_url = '/bookings/list/own'
    success_message = "Your booking was successfully updated."

    def test_func(self):
        return self.request.user == self.get_object().owner.user


class DeleteBooking(
        LoginRequiredMixin,
        UserPassesTestMixin,
        SuccessMessageMixin,
        DeleteView):
    """ Delete a booking """
    model = Booking
    success_url = '/bookings/list/all'
    success_message = "Your booking was successfully deleted."

    # Either the owner of the booking or a superuser can delete it
    def test_func(self):
        booking = self.get_object()
        user = self.request.user
        return user.is_superuser or self.request.user == self.get_object().owner.user

    # https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBooking, self).delete(request, *args, **kwargs)
