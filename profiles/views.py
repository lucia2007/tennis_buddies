from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# to display messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.urls import reverse_lazy

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
    success_message = "Your Contact Info was successfully updated."

    def test_func(self):
        """
        Checks if the signed-in user is the same user who owns the profile.
        """
        return self.request.user == self.get_object().user

    def get_context_data(self, **kwargs):
        """
        Pass the generated URL to the template context
        """
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        profile_detail_url = reverse_lazy("profile-detail", kwargs={'pk': pk})
        context['profile_detail_url'] = profile_detail_url
        return context

    # https://stackoverflow.com/questions/26548018/how-to-feed-success-url-with-pk-from-saved-model
    def get_success_url(self):
        """
        Get the primary key from the updated user.
        Get the success_url after updating the user's contact info.
        """
        pk = self.object.pk

        # Redirect to the user's updated contact-detail page
        return reverse_lazy("profile-detail", kwargs={'pk': pk})


class AddUserProfile(LoginRequiredMixin, CreateView):
    """ Add user profile view """
    template_name = 'profiles/add.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('profile-detail', kwargs={'pk': None})

    # Lets me specify 'next' page after success
    # https://stackoverflow.com/questions/64040028/how-to-redirect-to-the-next-url-instead-of-the-success-url-in-a-generic-class-b
    def get_success_url(self):
        """
        Get success_url after creating the user profile. If there is a 'next'
        parameter, take the user to "url", else default to success_url.
        """
        url = self.request.GET.get('next')
        if url:
            return url
        else:
            return reverse_lazy(
                'profile-detail',
                kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        """
        Process the valid form and display success message.
        """
        form.instance.user = self.request.user
        messages.success(
            self.request, f"Your contact info was saved successfully."
            )
        return super().form_valid(form)


class DeleteUserProfile(
        LoginRequiredMixin,
        UserPassesTestMixin,
        SuccessMessageMixin,
        DeleteView):
    """ Delete User Profile (contact info) """
    model = UserProfile
    success_url = '/'
    success_message = "All your information has been successfully deleted."

    def get_context_data(self, **kwargs):
        """
        Pass the generated URL to the template context
        """
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        profile_detail_url = reverse_lazy("profile-detail", kwargs={'pk': pk})
        context['profile_detail_url'] = profile_detail_url
        return context

    def test_func(self):
        """
        Checks if the signed in user is the same user who owns the object
        """
        return self.request.user == self.get_object().user

    # https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteUserProfile, self).delete(request, *args, **kwargs)
