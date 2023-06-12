from django.shortcuts import render
from django_tables2 import SingleTableView
from django.views.generic import ListView
from .tables import BookingCalendarTable
from bookings.models import TIMES, COURT_NAME, Booking, Court
from datetime import datetime, date
from django.utils import timezone


class BookingCalendarListView(SingleTableView):
    # model = BookingCalendar
    queryset = [{'time': item[0]} for item in TIMES]
    table_class = BookingCalendarTable
    template_name = 'bookingcalendar/calendar.html'

    def get_queryset(self) -> list[dict[str, str]]:
        dict_list = []
        d = date(2023, 6, 12)
        court_id = Court.objects.get(name="one").id
        for item in TIMES:
            if Booking.objects.filter(date=d, time=item[0], court=court_id).count() >=1:
                availability = "booked"
            else:
                availability = "free"
            dictionary = {'hour': item[0], 'one': availability}
            dict_list.append(dictionary)
        return dict_list

