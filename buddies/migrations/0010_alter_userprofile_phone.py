# Generated by Django 3.2.19 on 2023-05-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("buddies", "0009_alter_userprofile_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
