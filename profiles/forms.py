from django import forms
from .models import UserProfile
from django.core.validators import RegexValidator

# https://regex101.com/
phone_validator = RegexValidator(
    regex=r'^\+353\d{9}$',
    message="Phone number must be in format: '+353999999999'",
    )

# https://salesforce.stackexchange.com/questions/41153/best-regex-for-first-last-name-validation
firstname_validator = RegexValidator(
    # regex=r'^[^±!@£$%^&*_+§¡€#¢§¶•ªº«\\/<>?:;|=.,0-9]{1,20}$',
    regex=r"^[ \u00c0-\u01ffa-zA-Z'\-]+$",
    message="First name should not contain numbers or special characters."
    )

lastname_validator = RegexValidator(
    regex=r"^[ \u00c0-\u01ffa-zA-Z'\-]+$",
    message="Last name should not contain numbers or special characters."
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

    phone = forms.CharField(
        max_length=13, required=True,
        validators=[phone_validator],
        widget=forms.TextInput(attrs={'placeholder': '+353xxxxxxxxx'})
    )
    first_name = forms.CharField(max_length=20, required=True, validators=[firstname_validator])
    last_name = forms.CharField(max_length=20, required=True, validators=[lastname_validator])
