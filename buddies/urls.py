from django.urls import path
from .views import AddBuddy, Buddies, BuddyDetail, DeleteBuddy, EditBuddy

urlpatterns = [
    path("add/", AddBuddy.as_view(), name="add-buddy"),
    path("", Buddies.as_view(), name="buddies"),
    path("<slug:pk>", BuddyDetail.as_view(), name="buddy-detail"),
    path("delete/<slug:pk>", DeleteBuddy.as_view(), name="delete-buddy"),
    path("edit/<slug:pk>", EditBuddy.as_view(), name="edit-buddy"),
]
