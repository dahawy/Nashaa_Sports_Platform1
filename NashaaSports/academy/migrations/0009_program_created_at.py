# Generated by Django 4.2.14 on 2024-08-24 04:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_program_admin_activtion_alter_program_sport_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
