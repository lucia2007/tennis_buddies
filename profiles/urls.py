from django.urls import path
from .views import AddUserProfile

urlpatterns = [
    path(
        "delete/<slug:pk>/",
        DeleteUserProfile.as_view(),
        name="delete-profile"
        ),
]