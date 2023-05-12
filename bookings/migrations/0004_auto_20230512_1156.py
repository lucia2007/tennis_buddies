# Generated by Django 3.2.19 on 2023-05-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20230512_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('09:00 - 10:00', '09:00 - 10:00'), ('10:00 - 11:00', '10:00 - 11:00'), ('11:00 - 12:00', '11:00 - 12:00'), ('12:00 - 13:00', '12:00 - 13:00'), ('13:00 - 14:00', '13:00 - 14:00'), ('14:00 - 15:00', '14:00 - 15:00'), ('15:00 - 16:00', '15:00 - 16:00'), ('16:00 - 17:00', '17:00 - 18:00'), ('18:00 - 19:00', '18:00 - 19:00'), ('19:00 - 20:00', '19:00 - 20:00'), ('21:00 - 22:00', '21:00 - 22:00')], default='09:00 - 10:00', max_length=15),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(choices=[('09:00 - 10:00', '09:00 - 10:00'), ('10:00 - 11:00', '10:00 - 11:00'), ('11:00 - 12:00', '11:00 - 12:00'), ('12:00 - 13:00', '12:00 - 13:00'), ('13:00 - 14:00', '13:00 - 14:00'), ('14:00 - 15:00', '14:00 - 15:00'), ('15:00 - 16:00', '15:00 - 16:00'), ('16:00 - 17:00', '17:00 - 18:00'), ('18:00 - 19:00', '18:00 - 19:00'), ('19:00 - 20:00', '19:00 - 20:00'), ('21:00 - 22:00', '21:00 - 22:00')], default='09:00 - 10:00', max_length=15),
        ),
    ]
