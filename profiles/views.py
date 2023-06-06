from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# to make sure the user is logged in
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from .forms import UserProfileForm


# CRUD functionality was done following Dee Mc's Recipe tutorial:
# https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy
class ProfileDetail(DetailView):
    """ View a single profile """
    template_name = 'profiles/detail.html'
    model = UserProfile
    context_object_name = "profile"


class EditUserProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit Contact Info """
    template_name = 'profiles/edit.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = '/buddies/'  # change this to profile-detail

    def test_func(self):
        """
        Checks if the signed in user is the same user who owns the profile
        """
        return self.request.user == self.get_object().user


class AddUserProfile(LoginRequiredMixin, CreateView):
    """ Add user profile view """
    template_name = 'profiles/add.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = '/'

    # Lets me specify 'next' page after success
    # https://stackoverflow.com/questions/64040028/how-to-redirect-to-the-next-url-instead-of-the-success-url-in-a-generic-class-b
    def get_success_url(self):
        url = self.request.GET.get('next', self.success_url)
        return url

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteUserProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete User Profile (contact info) """
    model = UserProfile
    success_url = '/'

    def test_func(self):
        """
        Checks if the signed in user is the same user who owns the object
        """
        return self.request.user == self.get_object().user
