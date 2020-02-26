from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ExifTags

class Profile(models.Model):
    cities = [('İstanbul','İstanbul'),('Ankara','Ankara'),('İzmir','İzmir'),('Diğer','Diğer')]
    kredi_tutari_opts = [('Yok','Yok'),('5.000 TL','5.000 TL'),('10.000 TL','10.000 TL'),('15.000 TL','15.000 TL'),('20.000 TL','20.000 TL'),('25.000 TL','25.000 TL'),('30.000TL','30.000TL'),('35.000 TL','35.000 TL'),('40.000 TL','40.000 TL'),('45.000 TL','45.000 TL'),('50.000 TL','50.000 TL'),('60.000 TL ve üzeri','60.000 TL ve üzeri')]
    kredi_talebi_opts = [('10.000 TL','10.000 TL'),('15.000 TL','15.000 TL'),('20.000 TL','20.000 TL'),('25.000 TL','25.000 TL'),('30.000TL','30.000TL'),('35.000 TL','35.000 TL'),('40.000 TL','40.000 TL'),('45.000 TL','45.000 TL'),('50.000 TL','50.000 TL'),('60.000 TL ve üzeri','60.000 TL ve üzeri')]
    banks = [('AKBANK','AKBANK'),('AKTİFBANK','AKTİFBANK'),('BURGAN','BURGAN'),('DENİZBANK','DENİZBANK'),('HALK BANKASI','HALK BANKASI'),('GARANTİ BBVA','GARANTİ BBVA'),('HSBC','HSBC'),('ING BANK','ING BANK'),('İŞ BANKASI','İŞ BANKASI'),('ODEA','ODEA'),('VAKIF BANK','VAKIF BANK'),('QNB FİNANSBANK','QNB FİNANSBANK'),('YAPI KREDİ','YAPI KREDİ'),('ZİRAAT BANKASI','ZİRAAT BANKASI'),('DİĞER','DİĞER')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='Default_User.png', upload_to='profile_pics',verbose_name='Profil Foto')
    tc = models.CharField(verbose_name='Tc',max_length=11,blank=True, null=True)
    ad = models.CharField(max_length=15,verbose_name='Ad',blank=True, null=True)
    soyad = models.CharField(max_length=15,verbose_name='Soyad',blank=True, null=True)
    # tel = models.CharField(verbose_name='Tel',max_length=11)
    tel = models.CharField(max_length=11, blank=True, null=True) # validators should be a list
    maas_banka = models.CharField(verbose_name='Maaş Bankası',max_length=20,choices=banks,blank=True, null=True)
    kredi_tutari = models.CharField(max_length=18,verbose_name='Kredi Mevcut',choices=kredi_tutari_opts,blank=True, null=True)
    kredi_talebi= models.CharField(max_length=18,verbose_name='Kredi Talebi',choices=kredi_talebi_opts,blank=True, null=True)
    city = models.CharField(max_length=20,choices=cities,verbose_name='Şehir',blank=True, null=True)
    join_date = models.DateTimeField(verbose_name='Kayıt Tarihi',auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Güncelleme Tarihi',auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profili'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        try:
            if hasattr(img, '_getexif'): # only present in JPEGs
                for orientation in ExifTags.TAGS.keys(): 
                    if ExifTags.TAGS[orientation]=='Orientation':
                        break 
                e = img._getexif()       # returns None if no EXIF data
                if e is not None:
                    exif=dict(e.items())
                    orientation = exif[orientation] 
                    if orientation == 3:   img = img.transpose(Image.ROTATE_180)
                    elif orientation == 6: img = img.transpose(Image.ROTATE_270)
                    elif orientation == 8: img = img.transpose(Image.ROTATE_90)
        except:
            return img
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)