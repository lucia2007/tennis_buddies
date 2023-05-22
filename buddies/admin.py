from django.contrib import admin  # type: ignore
from .models import UserProfile, Buddy
from django_summernote.admin import SummernoteModelAdmin  # type: ignore


@admin.register(Buddy)
class BuddyAdmin(SummernoteModelAdmin):
    list_display = (
        "get_user_name",
        "is_approved",
        "status",
        "gender",
        "level",
        "game_type",
        "availability",
        "practice_type",
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
        queryset.update(is_approved=True)


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = (
#         'first_name',
#         'last_name',
#         'phone',
#         'created_on')
#     list_filter = ('first_name', 'created_on')
#     search_fields = ['first_nane', 'last_name', 'phone']
