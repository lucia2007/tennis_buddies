from django.db import models
# Import User model from the Django auth app
from django.contrib.auth.models import User
# Import Cloudinary for storing images
from cloudinary.models import CloudinaryField  # type: ignore
from datetime import date
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(
        max_length=20,
        null=True)
    # validators=[RegexValidator(r'^\+?\d{9, 15}$')])  # validate if phone#
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
    # change placeholder text
    profile_picture = CloudinaryField('image', default='placeholder')
    picture_description = models.CharField(max_length=200)
    # add picture description
    # excerpt = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=1)
    gender = models.CharField(max_length=6, choices=[
                              ('M', 'Male'),
                              ('F', 'Female')])
    level = models.CharField(max_length=15, choices=[
                              ('Beginner', 'Beginner'),
                              ('Intermediate', 'Intermediate'),
                              ('Advanced', 'Advanced')])
    practice_type = models.CharField(max_length=25, choices=[
                              ('Hitting Practice', 'Hitting Practice'),
                              ('Match Practice', 'Match Practice'),
                              ('Both', 'Both')])
    game_type = models.CharField(max_length=10, choices=[
                              ('Singles', 'Singles'),
                              ('Doubles', 'Doubles'),
                              ('Both', 'Both')])
    availability = models.CharField(max_length=10, choices=[
                              ('Morning', 'Morning'),
                              ('Afternoon', 'Afternoon'),
                              ('Both', 'Both')])
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns strings representation of an object """
        return self.user_profile.first_name
