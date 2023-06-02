from django.urls import path
from .views import AddBooking, Bookings, BookingDetail
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path('add/', AddBooking.as_view(), name='add-booking'),
    path('bookings/', Bookings.as_view(), name='bookings'),
    path('<slug:pk>/', BookingDetail.as_view(), name='booking-detail'),
]
