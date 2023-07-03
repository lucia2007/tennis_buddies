from django.contrib import admin  # type: ignore
from .models import UserProfile, Buddy
from django_summernote.admin import SummernoteModelAdmin  # type: ignore


@admin.register(Buddy)
class BuddyAdmin(SummernoteModelAdmin):
    """
    Display Buddy details in admin panel
    """
    list_display = (
        'pk',
        "get_user_name",
        'user_profile',
        "is_approved",
        "status",
        "gender",
        "level",
        "game_type",
        "availability",
        "practice_type",
        "email",
        "created_on",
    )

    @admin.display(ordering="user_profile__first_name", description="name")
    def get_user_name(self, obj):
        return obj.user_profile.first_name + " " + obj.user_profile.last_name

    search_fields = ["user_profile", "about_me"]
    list_filter = ("user_profile", "status", "created_on")
    summernote_fields = "about_me"
    actions = ["approve_buddy"]

    def approve_buddy(self, request, queryset):
        """
        This will be finished in the next version.
        """
        queryset.update(is_approved=True)
