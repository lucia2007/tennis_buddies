from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from datetime import datetime
from profiles.models import UserProfile
from cloudinary.models import CloudinaryField  # type: ignore


class Court(models.Model):
    NAME = [('one', 'One'), ('two', 'Two'), ('three', 'Three'),
            ('four', 'Four'), ('five', 'Five')]
    court_name = models.CharField(max_length=5, choices=NAME)

    def __str__(self):
        return self.court_name


TIMES = [
    ('09:00 - 10:00', '09:00 - 10:00'),
    ('10:00 - 11:00', '10:00 - 11:00'),
    ('11:00 - 12:00', '11:00 - 12:00'),
    ('12:00 - 13:00', '12:00 - 13:00'),
    ('13:00 - 14:00', '13:00 - 14:00'),
    ('14:00 - 15:00', '14:00 - 15:00'),
    ('15:00 - 16:00', '15:00 - 16:00'),
    ('16:00 - 17:00', '16:00 - 17:00'),
    ('17:00 - 18:00', '17:00 - 18:00'),
    ('18:00 - 19:00', '18:00 - 19:00'),
    ('19:00 - 20:00', '19:00 - 20:00'),
    ('21:00 - 22:00', '21:00 - 22:00')]


class Booking(models.Model):
    """
    This class enables a signed in user to book a court up to 7 days
    in advance, max 1 court per day
    """

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(
            max_length=15, choices=TIMES, default="09:00 - 10:00")
    # maximum one booking per user per day
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    opponents = models.ManyToManyField(
        UserProfile, related_name="booking_opponents")
    email_sent = models.BooleanField(default=False)

    # to enable ordering
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.user.username)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    time = models.CharField(
            max_length=15, choices=TIMES, default="09:00 - 10:00")
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=25, choices=[
                              ('Coaching', 'Coaching'),
                              ('Tournament', 'Tournament'),
                              ('Social', 'Social')])

    def __str__(self):
        return self.user.username
