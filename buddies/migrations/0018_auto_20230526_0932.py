# Generated by Django 3.2.19 on 2023-05-26 09:32

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20230526_0932'),
        ('buddies', '0017_alter_buddy_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buddy',
            name='about_me',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='availability',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Both', 'Both')], default='Both', max_length=10),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='date_of_birth',
            field=models.DateField(default='2003-12-01'),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='game_type',
            field=models.CharField(choices=[('Singles', 'Singles'), ('Doubles', 'Doubles'), ('Both', 'Both')], default='Singles', max_length=10),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=15),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='picture_description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='practice_type',
            field=models.CharField(choices=[('Hitting Practice', 'Hitting Practice'), ('Match Practice', 'Match Practice'), ('Both', 'Both')], default='Both', max_length=25),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='buddy',
            name='user_profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buddy', to='profiles.userprofile'),
        ),
    ]
