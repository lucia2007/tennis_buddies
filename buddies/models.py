from django.db import models
# Import User model from the Django auth app
from django.contrib.auth.models import User
# Import Cloudinary for storing images
from cloudinary.models import CloudinaryField  # type: ignore
from datetime import date
from django.core.validators import RegexValidator
from profiles.models import UserProfile
from django.core.exceptions import ValidationError


class Buddy(models.Model):
    """
    A model to create and manage Tennis Buddy profiles.
    """
    STATUS = ((0, "inactive"), (1, "active"))
    user_profile = models.OneToOneField(
        UserProfile, related_name="buddy", on_delete=models.CASCADE
    )
    about_me = models.TextField(default="Describe yourself")
    date_of_birth = models.DateField(default="2003-12-01")
    profile_picture = CloudinaryField("image", default="placeholder")
    picture_description = models.CharField(
        max_length=200, default="A picture of me"
        )
    is_approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=1)
    gender = models.CharField(max_length=6, choices=[
        ("Male", "Male"), ("Female", "Female")], default="M")
    level = models.CharField(
        max_length=15,
        choices=[
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
        ],
        default="Beginner"
    )
    practice_type = models.CharField(
        max_length=50,
        choices=[
            ("Hitting Practice", "Hitting Practice"),
            ("Match Practice", "Match Practice"),
            (
             "Both Match and Hitting Practice",
             "Both Match and Hitting Practice"
            ),
        ],
        default="Both"
        )
    game_type = models.CharField(
        max_length=50,
        choices=[
            ("Singles", "Singles"),
            ("Doubles", "Doubles"),
            ("Both Singles and Doubles", "Both Singles and Doubles")],
        default="Singles"
        )
    availability = models.CharField(
        max_length=50,
        choices=[
            ("Morning", "Morning"),
            ("Afternoon", "Afternoon"),
            ("Both Morning and Afternoon", "Both Morning and Afternoon")],
        default="Both"
        )
    email = models.EmailField(max_length=150)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns strings representation of an object"""
        return f"{self.user_profile.first_name} - {self.user_profile.email}"
