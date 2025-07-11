# Generated by Django 5.1.6 on 2025-03-23 12:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="frequency",
            field=models.CharField(
                blank=True,
                choices=[
                    ("m x-y * * *", "every hour"),
                    ("m x-y/2 * * *", "every 2 hours"),
                    ("m x-y/2 * * *", "every 3 hours"),
                    ("m x,z,y * * *", "3 times per day"),
                    ("m x,y * * *", "2 times per day"),
                    ("m h * * *", "every day"),
                    ("m h */2 * *", "every 2 days"),
                    ("m h */3 * *", "every 3 days"),
                    ("m h * * d", "selected days"),
                ],
                default="m h * * *",
                help_text="Select how often a good habit should be performed. NOTE! A good habit should be performed once a week at least. For good habits only!",
                null=True,
                verbose_name="frequency",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.DateTimeField(
                blank=True,
                help_text="Enter the time when a habit should be performed. In case a habit should be performed several times per day, the end time should also be selected. For good habits only!",
                null=True,
                verbose_name="time",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="habits",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
