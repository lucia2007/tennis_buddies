from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView)

# to make sure the user is logged in
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.contrib import messages

# to display messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Buddy
from .forms import BuddyForm

# for search functionality
from django.db.models import Q


# CRUD functionality was done following Dee Mc's Recipe tutorial: 
# https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy
class Buddies(ListView):
    """View all buddies"""

    template_name = "buddies/buddies.html"
    model = Buddy
    context_object_name = "buddies"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            buddies = self.model.objects.filter(
                Q(level__icontains=query) |
                Q(game_type__icontains=query) |
                Q(availability__icontains=query) |
                Q(practice_type__icontains=query) |
                Q(gender__icontains=query)
                )
            if not buddies:
                messages.success(
                    self.request,
                    f"There is no match for your search. Try a different keyword."
                    )
        else:
            buddies = self.model.objects.all()
        return buddies


class BuddyDetail(LoginRequiredMixin, DetailView):
    """View a single Buddy profile"""

    template_name = "buddies/buddy_detail.html"
    model = Buddy
    context_object_name = "buddy"


class AddBuddy(LoginRequiredMixin, CreateView):
    """Add buddy view"""

    template_name = "buddies/add.html"
    model = Buddy
    form_class = BuddyForm
    success_url = "/buddies/"

    def form_valid(self, form):
        form.instance.user_profile = self.request.user.user_profile
        messages.success(
            self.request, f"Your Buddy Profile was created successfully."
            )
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

class EditBuddy(
        LoginRequiredMixin,
        UserPassesTestMixin,
        SuccessMessageMixin,
        UpdateView
        ):
    """" Edit User Buddy Profile """
    template_name = "buddies/edit.html"
    model = Buddy
    form_class = BuddyForm
    success_message = "Your Buddy Profile was successfully updated."

    def test_func(self):
        """
        Checks if the signed in user is the same user who owns the object
        """
        return self.request.user == self.get_object().user_profile.user


class DeleteBuddy(
        LoginRequiredMixin,
        UserPassesTestMixin,
        SuccessMessageMixin,
        DeleteView):
    """ Delete a buddy profile """
    model = Buddy
    success_url = '/buddies/'
    success_message = "Your Buddy Profile was successfully deleted."

    def test_func(self):
        """
        Checks if the signed in user is the same user who owns the object
        """
        return self.request.user == self.get_object().user_profile.user

    # https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteBuddy, self).delete(request, *args, **kwargs)
