from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from datetime import datetime
from profiles.models import UserProfile
from cloudinary.models import CloudinaryField  # type: ignore
from django.utils import timezone
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError

from psycopg2.extras import DateTimeTZRange  # type: ignore
# from django.utils import timezone
# from datetime import timedelta

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


# https://stackoverflow.com/questions/64362067/django-datetimerangefield-default-timezone-now-timezone-now10years
# def next_seven_days():
#     now = timezone.now()

#     return DateTimeTZRange(now, now + timedelta(days=7))


class Booking(models.Model):
    """
    This class enables a signed in user to book a court up to 7 days
    in advance, max 1 court per day
    """

    owner = models.ForeignKey(
                            UserProfile,
                            on_delete=models.CASCADE,
                            )
    date = models.DateField(default=timezone.now)
    # date = models.DateTimeRangeField(default=next_seven_days())
    time = models.CharField(
            max_length=15, choices=TIMES, default="09:00 - 10:00")
    # maximum one booking per user per day
    court = models.ForeignKey(Court, on_delete=models.CASCADE, default='one')
    opponents = models.ManyToManyField(
        UserProfile, related_name="booking_opponents")
    email_sent = models.BooleanField(default=False)

    # to enable ordering
    class Meta:
        ordering = ['-date']
        constraints = [
            models.UniqueConstraint(
                fields=["date", "time", "court"], name="unique_booking"
            )
        ]

    # def clean(self):
    #     # Check if the owner already has a booking on the selected date
    #     existing_booking = Booking.objects.filter(
    #         owner=self.owner,
    #         date=self.date
    #     ).exclude(pk=self.pk).first()

    #     if existing_booking:
    #         raise ValidationError(
    #             "You can only make one reservation per day."
    #             " Please make a booking for a different date.")

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
