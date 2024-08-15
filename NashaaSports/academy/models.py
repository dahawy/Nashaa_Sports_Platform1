from django.db import models
from account.models import AcademyProfile

class Branch(models.Model):
    class Cities(models.TextChoices):
        RIYADH = 'RYD', 'الرياض'
        JEDDAH = 'JED', 'جدة'
        MAKKAH = 'MKK', 'مكة المكرمة'
        MADINAH = 'MDN', 'المدينة المنورة'
        DAMMAM = 'DAM', 'الدمام'
        KHOBAR = 'KBR', 'الخبر'
        DHAHRAN = 'DHR', 'الظهران'
        ABHA = 'ABH', 'أبها'
        TAIF = 'TIF', 'الطائف'
        TABUK = 'TBU', 'تبوك'
        ALKHARJ = 'ALK', 'الخرج'
        ALQASSIM = 'QSM', 'القصيم'
        ALHASA = 'HAS', 'الأحساء'
        HAIL = 'HAIL', 'حائل'
        JUBAIL = 'JBL', 'الجبيل'
        NAJRAN = 'NJR', 'نجران'
        JAZAN = 'JZN', 'جازان'
        YANBU = 'YNB', 'ينبع'
        RAS_TANURA = 'RAS', 'رأس تنورة'
        QATIF = 'QTF', 'القطيف'
        BURAIDAH = 'BRD', 'بريدة'
        ALKHAFJI = 'KHF', 'الخفجي'

    academy = models.ForeignKey(AcademyProfile, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=128)
    branch_location = models.URLField()
    branch_city = models.CharField(choices=Cities.choices, default=Cities.RIYADH)
    register_no = models.CharField(max_length=64)

class Program(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=255)
    description = models.TextField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_seats = models.IntegerField()
    age_group = models.CharField(max_length=64)
class Coach(models.Model):
    class Gender(models.TextChoices):
        Male = 'Male', 'ذكر'
        Female = 'Female' , 'أنثى'
    class Nationality(models.TextChoices):
        EGYPTIAN = 'EG', 'مصري'
        SAUDI = 'SA', 'سعودي'
        ALGERIAN = 'DZ', 'جزائري'
        EMIRATI = 'AE', 'إماراتي'
        AMERICAN = 'US', 'أمريكي'
        IRAQI = 'IQ', 'عراقي'
        JORDANIAN = 'JO', 'أردني'
        BRITISH = 'GB', 'بريطاني'
        KUWAITI = 'KW', 'كويتي'
        LEBANESE = 'LB', 'لبناني'
        LIBYAN = 'LY', 'ليبي'
        MOROCCAN = 'MA', 'مغربي'
        OMANI = 'OM', 'عماني'
        PALESTINIAN = 'PS', 'فلسطيني'
        QATARI = 'QA', 'قطري'
        SYRIAN = 'SY', 'سوري'
        SUDANESE = 'SD', 'سوداني'
        TUNISIAN = 'TN', 'تونسي'
        YEMENI = 'YE', 'يمني'
        BAHRAINI = 'BH', 'بحريني'
        SOMALI = 'SO', 'صومالي'
        MAURITANIAN = 'MR', 'موريتاني'

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    experience = models.IntegerField()
    nationality = models.CharField(max_length=64, choices=Nationality.choices, default=Nationality.SAUDI)
    gender = models.CharField( choices=Gender.choices)
    avatar = models.ImageField(upload_to='coach_avatars/')
    created_at = models.DateTimeField(auto_now_add=True)

class TimeSlot(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

class ProgramImage(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='program_images/')

class ProgramVideo(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    video = models.FileField(upload_to='program_videos/')


