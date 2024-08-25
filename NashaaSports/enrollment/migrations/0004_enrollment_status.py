# Generated by Django 4.2.14 on 2024-08-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enrollment", "0003_enrollment_time_slot"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "معلق"),
                    ("in_progress", "جاري"),
                    ("Ended", "منتهي"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
