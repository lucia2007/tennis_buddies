from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from datetime import datetime
from profiles.models import UserProfile
from cloudinary.models import CloudinaryField  # type: ignore
from django.utils import timezone
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError

from psycopg2.extras import DateTimeTZRange  # type: ignore

from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import DateTimeRangeField, RangeOperators

COURT_NAME = [
    ('one', 'One'),
    ('two', 'Two'),
    ('three', 'Three'),
    ('four', 'Four'),
    ('five', 'Five')
    ]


class Court(models.Model):
    """ Create a class with given courts """
    name = models.CharField(max_length=5, choices=COURT_NAME)

    def __str__(self):
        return self.name


TIMES = [
    ('09:00-10:00', '09:00 - 10:00'),
    ('10:00-11:00', '10:00 - 11:00'),
    ('11:00-12:00', '11:00 - 12:00'),
    ('12:00-13:00', '12:00 - 13:00'),
    ('13:00-14:00', '13:00 - 14:00'),
    ('14:00-15:00', '14:00 - 15:00'),
    ('15:00-16:00', '15:00 - 16:00'),
    ('16:00-17:00', '16:00 - 17:00'),
    ('17:00-18:00', '17:00 - 18:00'),
    ('18:00-19:00', '18:00 - 19:00'),
    ('19:00-20:00', '19:00 - 20:00'),
    ('21:00-22:00', '21:00 - 22:00')]


class Booking(models.Model):
    """
    This model collects information about date, time, court, opponents
    and if an email was sent (future feature)
    """

    owner = models.ForeignKey(
                            UserProfile,
                            on_delete=models.CASCADE,
                            )
    date = models.DateField(default=timezone.now)
    time = models.CharField(
            max_length=15, choices=TIMES, default="09:00 - 10:00")
    court = models.ForeignKey(Court, on_delete=models.CASCADE, default='one')
    opponents = models.ManyToManyField(
        UserProfile, related_name="booking_opponents")
    email_sent = models.BooleanField(default=False)

    class Meta:
        """ To enable ordering """
        ordering = ['-date']
        constraints = [
            models.UniqueConstraint(
                fields=["date", "time", "court"], name="unique_booking"
            )
        ]

    def __str__(self):
        return str(self.owner)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    time = models.CharField(
            max_length=15, choices=TIMES, default="09:00 - 10:00")
    # time should be a many to many field for staff
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    # court should be a many to many field for staff
    event_type = models.CharField(max_length=25, choices=[
                              ('Coaching', 'Coaching'),
                              ('Tournament', 'Tournament'),
                              ('Social', 'Social')])

    def __str__(self):
        return self.user.username
