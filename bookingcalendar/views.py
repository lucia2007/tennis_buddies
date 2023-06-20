from django.shortcuts import render
from django_tables2 import SingleTableView
from django.views.generic import ListView
from .tables import BookingCalendarTable
from bookings.models import TIMES, COURT_NAME, Booking, Court
from datetime import datetime, date
from django.utils import timezone


class BookingCalendarListView(SingleTableView):
    table_class = BookingCalendarTable
    template_name = 'bookingcalendar/calendar.html'

    def get_queryset(self):
        dict_list = []
        # Get the date from the request parameters
        # Change the booking table details according to the chosen date
        date_param = self.request.GET.get('date')
        # The bookings are displayed for the current day by default, otherwise for the chosen date
        # Convert a string to datetime
        # https://www.freecodecamp.org/news/python-string-to-datetime-how-to-convert-an-str-to-a-date-time-with-strptime/
        d = timezone.datetime.strptime(date_param, '%Y-%m-%d').date() if date_param else timezone.now().date()
        courts = Court.objects.all()

        for item in TIMES:
            dictionary = {'hour': item[0]}
            for court in courts:
                bookings = Booking.objects.filter(date=d, time=item[0], court=court)
                # Checks if there is a booking for a particular date, time and court
                if bookings.exists():
                    # This selects the owner of the booking
                    owner = Booking.objects.filter(date=d, time=item[0], court=court).first().owner
                    dictionary[court.name] = "booked" + ', ' + f"owner: {owner}"
                    # dictionary[court.name] = f
                else:
                    dictionary[court.name] = "free" + ', ' + f"Date: {d}, Time: {item[0]}, Court: {court}"
            dict_list.append(dictionary)
        return dict_list
