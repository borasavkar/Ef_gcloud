from django.contrib import admin
from .models import Post,Basvuru,Mesaj

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['content','date_posted','author']
    list_display_links = list_display
    search_fields = list_display
    list_filter=['date_posted','author']
    # class Meta:
    
@admin.register(Basvuru)
class BasvuruAdmin(admin.ModelAdmin):
    list_display=['tc','soyad','tel','maas_banka','kredi_tutari','kredi_talebi','city','date_posted','ad']
    list_display_links = list_display
    search_fields = list_display
    list_filter=['date_posted','city','kredi_tutari']

@admin.register(Mesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display=['soyad','tel','email','mesaj','date_posted','ad']
    list_display_links = list_display
    search_fields = list_display
    list_filter=['date_posted']