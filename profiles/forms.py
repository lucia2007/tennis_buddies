from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Form to create a user profile with contact details """
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'phone',
        ]

    labels = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'phone': 'Phone Number',
    }
