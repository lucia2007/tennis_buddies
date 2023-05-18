from django.urls import path
from .views import AddBuddy

urlpatterns = [
    path('', AddBuddy.as_view(), name='add-buddy'),
    # path('', AddUserProfile.as_view(), name='add-profile'),
]
