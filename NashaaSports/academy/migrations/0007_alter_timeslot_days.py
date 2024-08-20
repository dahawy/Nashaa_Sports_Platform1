# Generated by Django 4.2.14 on 2024-08-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0006_remove_program_no_of_seats_timeslot_no_of_seats_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeslot",
            name="days",
            field=models.CharField(
                choices=[
                    ("sun", "الأحد"),
                    ("mon", "الاثنين"),
                    ("tue", "الثلاثاء"),
                    ("wed", "الأربعاء"),
                    ("thu", "الخميس"),
                    ("fri", "الجمعة"),
                    ("sat", "السبت"),
                ],
                default=None,
                max_length=255,
            ),
        ),
    ]
