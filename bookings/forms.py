from django import forms
from .models import Booking, Event


class BookingForm(forms.ModelForm):
    """ A form to create a booking """

    # Override clean method in order to restrict the max amount of opponents
    # https://stackoverflow.com/questions/20203806/limit-maximum-choices-of-manytomanyfield/20230270#20230270
    def clean_opponents(self):
        opponents = self.cleaned_data['opponents']
        if len(opponents) > 3:
            raise forms.ValidationError('You can add maximum 3 opponents')
        return opponents

    class Meta:
        model = Booking
        fields = [
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
