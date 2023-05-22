# Generated by Django 3.2.19 on 2023-05-19 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_alter_userprofile_user"),
        ("buddies", "0016_auto_20230518_1315"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buddy",
            name="user_profile",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buddy",
                to="profiles.userprofile",
            ),
        ),
    ]
