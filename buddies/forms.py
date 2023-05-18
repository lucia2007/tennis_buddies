from django import forms
# import summernote?
from .models import Buddy


# class UserProfileForm(forms.ModelForm):
#     """ Form to create a user profile """
#     class Meta:
#         model = UserProfile
#         fields = [
#             'first_name',
#             'last_name',
#             'phone',
#             # should the model have an email as well prefilled from the user sign up???
#         ]

#     labels = {
#         'first_name': 'First Name',
#         'last_name': 'Last Name',
#         'phone': 'Phone Number',
#     }


class BuddyForm(forms.ModelForm):
    """ Form to create a buddy profile """
    class Meta:
        model = Buddy
        fields = [
            # 'user_profile',
            'about_me',
            # 'date_of_birth',
            'profile_picture',
            'picture_description',
            'status',
            'gender',
            'level',
            'practice_type',
            'game_type',
            'availability'
        ]

    labels = {
        # 'user_profile': 'User Profile',
        'about_me': 'About Me',
        # 'date_of_birth': 'DOB',
        'profile_picture': 'Profile Picture',
        'picture_description': 'Your Name',
        'status': 'Status',
        'gender': 'Gender',
        'level': 'Level',
        'practice_type': 'Practice Type',
        'game_type': 'Game Type',
        'availability': 'Available'
    }
