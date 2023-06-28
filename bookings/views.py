from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from django.core.exceptions import ValidationError
from django.utils.http import urlencode
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
from profiles.models import UserProfile
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# CRUD functionality was done following Dee Mc's Recipe tutorial:
# https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy

# https://stackoverflow.com/a/42193610/15098344
class TestIfHasProfileMixin(UserPassesTestMixin):
    '''Check if user has profile. If yes, take him to add-booking.
       If not, take him to add contact details and then to add-booking.
    '''

    def test_func(self):
        try:
            UserProfile.objects.get(user=self.request.user)
            return True
        except UserProfile.DoesNotExist:
            return False

    def handle_no_permission(self):
        '''to:[login,Profile] will signup or create profiles'''
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        # https://stackoverflow.com/questions/64538729/how-to-url-encode-in-django-views
        return redirect(reverse('add-profile') + '?' + urlencode({'next': self.request.get_full_path()}))


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


class AddBooking(LoginRequiredMixin, TestIfHasProfileMixin, CreateView):
    """" Add booking view """
    template_name = 'bookings/add.html'
    model = Booking
    form_class = BookingForm
    success_url = '/bookings/list/own'

    # https://stackoverflow.com/questions/22083218/django-how-to-pre-populate-formview-with-dynamic-non-model-data
    def get_initial(self):
        # Prepopulate the AddBooking form with params from bookingcalendar
        initial = super().get_initial()
        date = self.request.GET.get('date')
        time = self.request.GET.get('time')
        court_name = self.request.GET.get('court')
        court = Court.objects.get(name=court_name)  # Retrieve the Court object based on the court name
        initial['date'] = date
        initial['time'] = time
        initial['court'] = court
        return initial

    def form_valid(self, form):
        """
        Updates the instance of the user to the current signed in user
        https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/#models-and-request-user
        Check if the booking is not in the past (date and time)
        https://stackoverflow.com/questions/73260028/how-can-i-check-if-date-is-passed-from-django-model
        """
        form.instance.owner = self.request.user.user_profile

        messages.success(self.request, f"Booking was created successfully.")
        booking_date = form.cleaned_data.get('date')
        booking_time = form.cleaned_data.get('time')
        # https://bobbyhadz.com/blog/python-split-string-and-get-last-element#split-a-string-and-get-the-first-element-in-python
        start_time_str = booking_time.split('-')[0].strip()
        # https://www.freecodecamp.org/news/python-string-to-datetime-how-to-convert-an-str-to-a-date-time-with-strptime/
        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        if booking_date < date.today() or start_time < datetime.now().time():
            messages.warning(self.request, f"You have made a booking in the past. Is that what you wanted?")

        # If form is valid, it leads to a reload.
        # It returns an object that represents the parent class.
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
    success_message = "Your booking was successfully updated."

    def get_success_url(self):
        # Determine the success URL based on if the user is a superuser and not the owner of the booking
        all_or_own = 'all' if self.request.user.is_superuser and self.request.user.user_profile != self.object.owner else 'own'
        return reverse_lazy('list-bookings', kwargs={'all_or_own': all_or_own})

    def test_func(self):
        booking = self.get_object()
        user = self.request.user
        return user.is_superuser or self.request.user == self.get_object().owner.user


class DeleteBooking(
        LoginRequiredMixin,
        UserPassesTestMixin,
        SuccessMessageMixin,
        DeleteView):
    """ Delete a booking """
    model = Booking
    success_url = reverse_lazy('list-bookings', kwargs={'all_or_own': 'own'})
    success_message = "Your booking was successfully deleted."

    def get_success_url(self):
        # Determine the success URL based on if the user is a superuser and not the owner of the booking
        all_or_own = 'all' if self.request.user.is_superuser and self.request.user.user_profile != self.object.owner else 'own'
        return reverse_lazy('list-bookings', kwargs={'all_or_own': all_or_own})

    # Either the owner of the booking or a superuser can delete it
    def test_func(self):
        booking = self.get_object()
        user = self.request.user
        return user.is_superuser or self.request.user == self.get_object().owner.user

    # https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBooking, self).delete(request, *args, **kwargs)
