from django.urls import path
from .views import AddBuddy, Buddies

urlpatterns = [
    path("", AddBuddy.as_view(), name="add-buddy"),
    path("buddies/", Buddies.as_view(), name="buddies"),
]
