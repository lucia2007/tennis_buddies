from django.views.generic import CreateView, ListView, DetailView

# to make sure the user is logged in
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Buddy
from .forms import BuddyForm


class Buddies(ListView):
    """View all buddies"""

    template_name = "buddies/buddies.html"
    model = Buddy
    context_object_name = "buddies"


class BuddyDetail(DetailView):
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
        return super().form_valid(form)
