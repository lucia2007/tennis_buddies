from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def contact(request):
    return render(request, "contact/contact.html", {})
