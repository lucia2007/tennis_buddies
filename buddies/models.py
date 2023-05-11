from django.db import models  # type: ignore
# Import User model from the Django auth app
from django.contrib.auth.models import User  # type: ignore
# Import Cloudinary for storing images
from cloudinary.models import CloudinaryField  # type: ignore
from datetime import date


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)  #validate if phone number
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Buddy(models.Model):
    """
    A model to create and manage Tennis Buddy profiles
    """

    STATUS = ((0, "inactive"), (1, "active"))

    user_profile = models.OneToOneField(
        UserProfile, related_name="profile_owner", on_delete=models.CASCADE)
    about_me = models.TextField()  # make it into RichTextField
    data_of_birth = models.DateField()
    profile_picture = CloudinaryField('image', default='placeholder')  # change placeholder text
    # excerpt = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=1)
    gender = models.CharField(max_length=6, choices=[
                              ('M', 'Male'), ('F', 'Female')])
    level = models.CharField(max_length=15, choices=[
                              ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    practice_type = models.CharField(max_length=25, choices=[
                              ('Hitting Practice', 'Hitting Practice'), ('Match Practice', 'Match Practice'), ('Both', 'Both')])
    game_type = models.CharField(max_length=10, choices=[
                              ('Singles', 'Singles'), ('Doubles', 'Doubles'), ('Both', 'Both')])
    availability = models.CharField(max_length=10, choices=[
                              ('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Both', 'Both')])
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns strings representation of an object """
        return self.user_profile.first_name
