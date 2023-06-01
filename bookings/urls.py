from django.urls import path
from .views import AddBooking
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path('add/', AddBooking.as_view(), name='add-booking'),
]
