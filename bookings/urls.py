from django.urls import path
from .views import AddBooking, Bookings, BookingDetail, DeleteBooking, EditBooking
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path('add/', AddBooking.as_view(), name='add-booking'),
    path('list/', Bookings.as_view(), name='list-bookings'),
    path('<slug:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('delete/<slug:pk>/', DeleteBooking.as_view(), name='delete-booking'),
    path('edit/<slug:pk>/', EditBooking.as_view(), name='edit-booking'),
]
