from django.db import models
# Import User model from the Django auth app
from django.contrib.auth.models import User
# Import Cloudinary for storing images
from cloudinary.models import CloudinaryField  # type: ignore
from datetime import date
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    # validators=[RegexValidator(r'^\+?\d{9, 15}$')])  # validate if phone#
    created_on = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.user.username
