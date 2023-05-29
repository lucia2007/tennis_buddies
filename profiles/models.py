from django.db import models
# Import User model from the Django auth app
from django.contrib.auth.models import User
# Import Cloudinary for storing images
from cloudinary.models import CloudinaryField  # type: ignore
from datetime import date
from django.core.validators import RegexValidator


# When a user registers, new profile is created, otherwise it updates + saves
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    # validators=[RegexValidator(r'^\+?\d{9, 15}$')])  # validate if phone#
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update user profile """
    if not hasattr(instance, 'user_profile') or instance.user_profile is None:
        UserProfile.objects.create(user=instance)
