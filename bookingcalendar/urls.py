from django.urls import path
from django.contrib import admin

from bookingcalendar.views import BookingCalendarListView

urlpatterns = [
    path("", BookingCalendarListView.as_view(), name='calendar')
]
