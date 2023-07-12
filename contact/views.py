from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# to display messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse


def contact(request):
    """
    Send an inquiry to CLI.
    https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
             'first_name': form.cleaned_data['first_name'],
             'last_name': form.cleaned_data['last_name'],
             'email': form.cleaned_data['email_address'],
             'message': form.cleaned_data['message'],
             }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    'lferencikova@gmail.com',
                    ['lferencikova@gmail.com']
                    )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your inquiry was sent successfully.')
            return redirect('home')
        else:
            messages.warning(
                request,
                'Your email is invalid. It should look like name@domain.com.'
                )

    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
