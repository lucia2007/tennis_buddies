from django import forms
from .models import UserProfile
from django.core.validators import RegexValidator

# https://regex101.com/
phone_validator = RegexValidator(
    regex=r'^\+353\d{9}$',
    message="Phone number must be in format: '+353999999999'",
    )


class UserProfileForm(forms.ModelForm):
    """
    Form to create a user profile with contact details.
    Phone number is validated to in format of +353xxxxxxxxx
    https://docs.djangoproject.com/en/4.2/ref/validators/
    """
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
    phone = forms.CharField(max_length=13, validators=[phone_validator])
