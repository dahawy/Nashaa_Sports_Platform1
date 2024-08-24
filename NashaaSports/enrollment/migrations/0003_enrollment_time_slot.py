# Generated by Django 4.2.14 on 2024-08-24 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0009_program_created_at'),
        ('enrollment', '0002_enrollment_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='time_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='academy.timeslot'),
        ),
    ]