from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # @admin.display(ordering='user_profile__first_name', description='name')
    # def get_user_name(self, obj):
    #     return obj.user_profile.first_name + " " + obj.user_profile.last_name

    list_display = (
        'first_name',
        'last_name',
        'phone',
        'created_on')
    list_filter = ('last_name', 'created_on')
    search_fields = ['first_nane', 'last_name', 'phone']
