from django.urls import path, re_path
from .views import (
        AddBooking,
        BookingListView,
        BookingDetail,
        DeleteBooking,
        EditBooking
        )
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path('add/', AddBooking.as_view(), name='add-booking'),
    # I got a tip from my husband to use the regular expression
    # to alternate ListViews depending on url pattern
    # https://docs.djangoproject.com/en/4.2/topics/db/queries/
    re_path(
        'list/(?P<all_or_own>all|own)/',
        BookingListView.as_view(),
        name='list-bookings'
        ),
    path('<slug:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('delete/<slug:pk>/', DeleteBooking.as_view(), name='delete-booking'),
    path('edit/<slug:pk>/', EditBooking.as_view(), name='edit-booking'),
]
