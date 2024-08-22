# Generated by Django 5.1 on 2024-08-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_alter_timeslot_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='admin_activtion',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='sport_category',
            field=models.CharField(choices=[('football', 'كرة القدم'), ('judo', 'جودو'), ('basketball', 'كرة السلة'), ('tennis', 'تنس'), ('swimming', 'السباحة'), ('volleyball', 'كرة الطائرة'), ('karate', 'كاراتيه'), ('boxing', 'ملاكمة'), ('table_tennis', 'تنس الطاولة'), ('gymnastics', 'جمباز'), ('water_polo', 'كرة الماء'), ('athletics', 'ألعاب القوى'), ('handball', 'كرة اليد'), ('taekwondo', 'تايكوندو'), ('arrows', 'سهام')], default='football', max_length=50),
        ),
    ]