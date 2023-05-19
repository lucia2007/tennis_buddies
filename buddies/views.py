from django.views.generic import CreateView

# to make sure the user is logged in
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Buddy
from .forms import BuddyForm


# class AddUserProfile(LoginRequiredMixin, CreateView):
#     """ Add user profile view """
#     template_name = 'profiles/add.html'
#     model = UserProfile
#     form_class = UserProfileForm
#     success_url = '/buddies/'
#     # the success url should be home maybe?

#     def form_valid(self, form):
#         form.instance.user_profile = self.request.user_profile
#         return super(AddUserProfile, self).form_valid(form)


class AddBuddy(LoginRequiredMixin, CreateView):
    """ Add buddy view """
    template_name = 'buddies/add.html'
    model = Buddy
    form_class = BuddyForm
    success_url = '/buddies/'

    def form_valid(self, form):
        form.instance.user_profile = self.request.user.user_profile
        return super().form_valid(form)
