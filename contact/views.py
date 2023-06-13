from django.shortcuts import render, redirect
from .models import *
# from django.contrib import messages
# to display messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail (
            'message-from ' + message_name,  # Subject
            message,  # Message
            message_email,  # Email from
            ['lferencikova@gmail.com'],  # Email to

        )


        return render(request, "contact/contact.html", {'message-name': message_name})
    else:
        return render(request, "contact/contact.html", {})
