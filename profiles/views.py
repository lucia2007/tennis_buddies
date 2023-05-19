from django.views.generic import CreateView

# to make sure the user is logged in
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from .forms import UserProfileForm


class AddUserProfile(LoginRequiredMixin, CreateView):
    """ Add user profile view """
    template_name = 'profiles/add.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = '/buddies/'
    # the success url should be home maybe?

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
