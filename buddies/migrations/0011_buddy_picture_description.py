# Generated by Django 3.2.19 on 2023-05-16 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buddies', '0010_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='buddy',
            name='picture_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
