# Generated by Django 4.2.14 on 2024-08-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0002_remove_program_age_group_program_is_available_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="registration_end_date",
            field=models.DateField(default="2024-12-31"),
        ),
    ]
