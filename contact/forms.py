from django import forms


class ContactForm(forms.Form):
    """
    Contact form entries for contacting the club.
    """
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(required=True, max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
