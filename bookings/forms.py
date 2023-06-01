from django import forms
from .models import Booking, Event


class BookingForm(forms.ModelForm):
    """ A form to create a booking """
    class Meta:
        model = Booking
        fields = [
            'owner',
            'date',
            'time',
            'court',
            'opponents'
        ]

        labels = {
            "owner": "Booking Owner",
            "date": "Date",
            "time": "Time",
            "court": "Court",
            "opponents": "Opponent/s",
        }


