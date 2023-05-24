# Generated by Django 3.2.19 on 2023-05-18 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("buddies", "0013_rename_data_of_birth_buddy_date_of_birth"),
    ]

    operations = [
        migrations.AddField(
            model_name="buddy",
            name="user",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buddy_profile_owner",
                to="auth.user",
            ),
            preserve_default=False,
        ),
    ]