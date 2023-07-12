from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    """
    Contact form entries for contacting the club.
    All entries are validated. Names are checked if they contain
    numbers or special characters (front-end validation).
    https://stackoverflow.com/q/13587392/15098344
    """

    first_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'pattern': r"^[ \u00c0-\u01ffa-zA-Z'\-]+$",
            'title': 'Please enter a valid first name (letters only).'
            })
    )
    last_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'pattern': r"^[ \u00c0-\u01ffa-zA-Z'\-]+$",
            'title': 'Please enter a valid last name (letters only).'
            })
    )
    email_address = forms.EmailField(
        required=True,
        max_length=150,
    )

    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    class Meta:
        fields = ['first_name', 'last_name', 'email_address', 'message']
