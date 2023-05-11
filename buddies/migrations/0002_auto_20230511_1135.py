# Generated by Django 3.2.19 on 2023-05-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buddy',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buddy',
            name='practice_type',
            field=models.CharField(choices=[('Hitting Practice', 'Hitting Practice'), ('Match Practice', 'Match Practice'), ('Both', 'Both')], max_length=25),
        ),
    ]
