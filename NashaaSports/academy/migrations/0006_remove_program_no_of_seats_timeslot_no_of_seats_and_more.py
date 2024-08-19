# Generated by Django 4.2.14 on 2024-08-18 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0005_timeslot_days"),
    ]

    operations = [
        migrations.RemoveField(model_name="program", name="no_of_seats",),
        migrations.AddField(
            model_name="timeslot",
            name="no_of_seats",
            field=models.IntegerField(default=0),
        ),
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
                default="sun",
                max_length=255,
            ),
        ),
    ]