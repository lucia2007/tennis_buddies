from django.db import models

# Import User model from the Django auth app
from django.contrib.auth.models import User

# Import Cloudinary for storing images
from cloudinary.models import CloudinaryField  # type: ignore
from datetime import date
from django.core.validators import RegexValidator
from profiles.models import UserProfile


class Buddy(models.Model):
    """
    A model to create and manage Tennis Buddy profiles
    """

    STATUS = ((0, "inactive"), (1, "active"))
    user_profile = models.OneToOneField(
        UserProfile, related_name="buddy", on_delete=models.CASCADE
    )
    about_me = models.TextField(default="Describe yourself")  # make it into RichTextField
    date_of_birth = models.DateField(default="2003-12-01")
    # change placeholder text
    profile_picture = CloudinaryField("image", default="placeholder")
    # image = ResizedImageField(
    #     size=[400, None], quality=75, upload_to='buddies/', force_format="WEBP",
    #     blank=False, null=False
    #
    # if you decide to use this format, you need to install pip3 install
    # django_resized, then freeze requirements and
    # from django_resized import ResizedImageField + pip install pillow?)
    picture_description = models.CharField(
        max_length=200, default="A picture of me"
        )
    is_approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=1)
    gender = models.CharField(max_length=6, choices=[
        ("M", "Male"), ("F", "Female")], default="M")
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
        max_length=25,
        choices=[
            ("Hitting Practice", "Hitting Practice"),
            ("Match Practice", "Match Practice"),
            ("Both", "Both"),
        ],
        default="Both"
    )
    game_type = models.CharField(
        max_length=10,
        choices=[
            ("Singles", "Singles"),
            ("Doubles", "Doubles"),
            ("Both", "Both")], default="Singles"
    )
    availability = models.CharField(
        max_length=10,
        choices=[
            ("Morning", "Morning"),
            ("Afternoon", "Afternoon"),
            ("Both", "Both")], default="Both"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns strings representation of an object"""
        return self.user_profile.first_name
