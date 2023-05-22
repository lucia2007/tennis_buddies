# Generated by Django 3.2.19 on 2023-05-12 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("buddies", "0007_auto_20230512_1237"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(
                max_length=20,
                null=True,
                validators=[django.core.validators.DecimalValidator(15, 0)],
            ),
        ),
    ]
