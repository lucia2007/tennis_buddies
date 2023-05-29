from django.urls import path
from .views import (
    AddUserProfile,
    ProfileDetail,
    DeleteUserProfile,
    EditUserProfile)

urlpatterns = [
    path('add/', AddUserProfile.as_view(), name='add-profile'),
    path("<slug:pk>/", ProfileDetail.as_view(), name="profile-detail"),
    path(
        "delete/<slug:pk>/",
        DeleteUserProfile.as_view(),
        name="delete-profile"
        ),
    path("edit/<slug:pk>/", EditUserProfile.as_view(), name="edit-profile"),
]
