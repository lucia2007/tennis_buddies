# Generated by Django 3.2.19 on 2023-05-18 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0008_auto_20230518_1315"),
        ("profiles", "0001_initial"),
        ("buddies", "0015_remove_buddy_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buddy",
            name="user_profile",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile_owner",
                to="profiles.userprofile",
            ),
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
