from django import forms
from .models import Buddy


class BuddyForm(forms.ModelForm):
    """ Form to create a buddy profile """
    class Meta:
        model = Buddy
        fields = [
            'about_me',
            'date_of_birth',
            'profile_picture',
            'picture_description',
            'status',
            'gender',
            'level',
            'practice_type',
            'game_type',
            'availability'
        ]

    labels = {
        'about_me': 'About Me',
        'date_of_birth': 'DOB',
        'profile_picture': 'Profile Picture',
        'picture_description': 'Your Name',
        'status': 'Status',
        'gender': 'Gender',
        'level': 'Level',
        'practice_type': 'Practice Type',
        'game_type': 'Game Type',
        'availability': 'Available'
    }
