from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin  # type:ignore


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Display User Profile details in admin panel.
    """
    list_display = (
        'pk',
        'user',
        'first_name',
        'last_name',
        'phone',
        'email',
        'created_on')
    list_filter = ('last_name', 'created_on')
    search_fields = ['first_nane', 'last_name', 'phone']
