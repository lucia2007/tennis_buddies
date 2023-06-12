from django.shortcuts import render
from django_tables2 import SingleTableView
from django.views.generic import ListView
from .tables import BookingCalendarTable
from bookings.models import TIMES

class BookingCalendarListView(SingleTableView):
    # model = BookingCalendar
    queryset = [{'time': item[0]} for item in TIMES]
    table_class = BookingCalendarTable
    template_name = 'bookingcalendar/calendar.html'
