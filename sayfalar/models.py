from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    content = models.TextField(verbose_name='Yorum')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Basvuru(models.Model):
    cities = [('İstanbul','İstanbul'),('Ankara','Ankara'),('İzmir','İzmir'),('Diğer','Diğer')]
    kredi_tutari_opts = [('Yok','Yok'),('5.000 TL','5.000 TL'),('10.000 TL','10.000 TL'),('15.000 TL','15.000 TL'),('20.000 TL','20.000 TL'),('25.000 TL','25.000 TL'),('30.000TL','30.000TL'),('35.000 TL','35.000 TL'),('40.000 TL','40.000 TL'),('45.000 TL','45.000 TL'),('50.000 TL','50.000 TL'),('60.000 TL ve üzeri','60.000 TL ve üzeri')]
    kredi_talebi_opts = [('10.000 TL','10.000 TL'),('15.000 TL','15.000 TL'),('20.000 TL','20.000 TL'),('25.000 TL','25.000 TL'),('30.000TL','30.000TL'),('35.000 TL','35.000 TL'),('40.000 TL','40.000 TL'),('45.000 TL','45.000 TL'),('50.000 TL','50.000 TL'),('60.000 TL ve üzeri','60.000 TL ve üzeri')]
    banks = [('AKBANK','AKBANK'),('AKTİFBANK','AKTİFBANK'),('BURGAN','BURGAN'),('DENİZBANK','DENİZBANK'),('HALK BANKASI','HALK BANKASI'),('GARANTİ BBVA','GARANTİ BBVA'),('HSBC','HSBC'),('ING BANK','ING BANK'),('İŞ BANKASI','İŞ BANKASI'),('ODEA','ODEA'),('VAKIF BANK','VAKIF BANK'),('QNB FİNANSBANK','QNB FİNANSBANK'),('YAPI KREDİ','YAPI KREDİ'),('ZİRAAT BANKASI','ZİRAAT BANKASI'),('DİĞER','DİĞER')]
    tc = models.CharField(verbose_name='Tc',max_length=11,blank=False)
    ad = models.CharField(max_length=15,verbose_name='Ad')
    soyad = models.CharField(max_length=15,verbose_name='Soyad')
    # tel = models.CharField(verbose_name='Tel',max_length=11)
    tel = models.CharField(max_length=11, blank=False) # validators should be a list
    maas_banka = models.CharField(verbose_name='Maaş Bankası',max_length=20,choices=banks)
    kredi_tutari = models.CharField(max_length=18,verbose_name='Kredi Mevcut',choices=kredi_tutari_opts)
    kredi_talebi= models.CharField(max_length=18,verbose_name='Kredi Talebi',choices=kredi_talebi_opts)
    city = models.CharField(max_length=20,choices=cities,verbose_name='Şehir')
    date_posted = models.DateTimeField(default=timezone.now,verbose_name='Başvuru Tarihi')

    def __str__(self):
        return self.tc

class Mesaj(models.Model):
    ad = models.CharField(max_length=15,verbose_name='Ad')
    soyad = models.CharField(max_length=15,verbose_name='Soyad')
    tel = models.CharField(verbose_name='Tel',max_length=11)
    email = models.EmailField(verbose_name="e-Posta",max_length=30)
    mesaj= models.TextField(verbose_name="Mesaj",max_length=500)
    date_posted = models.DateTimeField(default=timezone.now,verbose_name='Mesaj tarihi')

    def __str__(self):
        return self.email
