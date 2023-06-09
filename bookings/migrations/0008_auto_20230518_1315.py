# Generated by Django 3.2.19 on 2023-05-18 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('bookings', '0007_alter_booking_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='opponents',
            field=models.ManyToManyField(related_name='booking_opponents', to='profiles.UserProfile'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
    ]
