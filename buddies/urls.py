from django.urls import path
from .views import AddBuddy, Buddies, BuddyDetail, DeleteBuddy

urlpatterns = [
    path("", AddBuddy.as_view(), name="add-buddy"),
    path("buddies/", Buddies.as_view(), name="buddies"),
    path("<slug:pk>", BuddyDetail.as_view(), name="buddy-detail"),
    path("delete/<slug:pk>", DeleteBuddy.as_view(), name="delete-buddy"),
]
