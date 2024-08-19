# Generated by Django 4.2.14 on 2024-08-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerquery',
            name='sender_type',
            field=models.CharField(choices=[('Academy', 'أكاديمية'), ('Individual', 'فرد')], default='Individual'),
        ),
        migrations.AddField(
            model_name='customerquery',
            name='status',
            field=models.CharField(choices=[('Open', 'مفتوح'), ('Closed', 'مغلق')], default='Open'),
        ),
    ]