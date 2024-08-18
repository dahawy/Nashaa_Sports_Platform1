# Generated by Django 4.2.14 on 2024-08-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.TextField()),
                ('category', models.CharField(choices=[('Complaint', 'شكوى'), ('Query', 'استفسار'), ('Suggestion', 'اقتراح')], default='Query')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]