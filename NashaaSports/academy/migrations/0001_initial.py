# Generated by Django 4.2.14 on 2024-08-15 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=128)),
                ('branch_location', models.URLField()),
                ('branch_city', models.CharField(choices=[('RYD', 'الرياض'), ('JED', 'جدة'), ('MKK', 'مكة المكرمة'), ('MDN', 'المدينة المنورة'), ('DAM', 'الدمام'), ('KBR', 'الخبر'), ('DHR', 'الظهران'), ('ABH', 'أبها'), ('TIF', 'الطائف'), ('TBU', 'تبوك'), ('ALK', 'الخرج'), ('QSM', 'القصيم'), ('HAS', 'الأحساء'), ('HAIL', 'حائل'), ('JBL', 'الجبيل'), ('NJR', 'نجران'), ('JZN', 'جازان'), ('YNB', 'ينبع'), ('RAS', 'رأس تنورة'), ('QTF', 'القطيف'), ('BRD', 'بريدة'), ('KHF', 'الخفجي')], default='RYD')),
                ('register_no', models.CharField(max_length=64)),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.academyprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('no_of_seats', models.IntegerField()),
                ('age_group', models.CharField(max_length=64)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.branch')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='program_videos/')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='program_images/')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.program')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=32)),
                ('experience', models.IntegerField()),
                ('nationality', models.CharField(choices=[('EG', 'مصري'), ('SA', 'سعودي'), ('DZ', 'جزائري'), ('AE', 'إماراتي'), ('US', 'أمريكي'), ('IQ', 'عراقي'), ('JO', 'أردني'), ('GB', 'بريطاني'), ('KW', 'كويتي'), ('LB', 'لبناني'), ('LY', 'ليبي'), ('MA', 'مغربي'), ('OM', 'عماني'), ('PS', 'فلسطيني'), ('QA', 'قطري'), ('SY', 'سوري'), ('SD', 'سوداني'), ('TN', 'تونسي'), ('YE', 'يمني'), ('BH', 'بحريني'), ('SO', 'صومالي'), ('MR', 'موريتاني')], default='SA', max_length=64)),
                ('gender', models.CharField(choices=[('Male', 'ذكر'), ('Female', 'أنثى')])),
                ('avatar', models.ImageField(upload_to='coach_avatars/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.branch')),
            ],
        ),
    ]