from django.shortcuts import render
from django_tables2 import SingleTableView
from django.views.generic import ListView
from .tables import BookingCalendarTable
from bookings.models import TIMES, COURT_NAME, Booking, Court
from datetime import datetime, date
from django.utils import timezone


class BookingCalendarListView(SingleTableView):
    # queryset = [{'hour': item[0], 'one': "unavailable"} for item in TIMES]
    table_class = BookingCalendarTable
    template_name = 'bookingcalendar/calendar.html'

    # Initialize date_param
    def __init__(self, **kwargs):
        self.date_param = None
        super().__init__(**kwargs)

    # Get the date_param from the date picker
    def get_table(self, **kwargs):
        table = super().get_table(**kwargs)
        table.date_param = self.date_param
        return table

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
                if Booking.objects.filter(date=d, time=item[0], court=court).count() >=1:
                    dictionary[court.name] = "booked"
                else:
                    dictionary[court.name] = "free"
            dict_list.append(dictionary)
        return dict_list
