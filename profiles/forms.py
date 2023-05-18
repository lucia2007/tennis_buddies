from django import forms
# import summernote?
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Form to create a user profile """
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'phone',
            # should the model have an email as well prefilled from the user sign up???
        ]

    labels = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'phone': 'Phone Number',
    }
