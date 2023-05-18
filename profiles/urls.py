from django.urls import path
from .views import AddUserProfile

urlpatterns = [
    path('', AddUserProfile.as_view(), name='add-profile'),
]