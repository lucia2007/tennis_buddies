from django.db import models
# Import User model from the Django auth app
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    """
    User Contact Details
    """
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.user.username
