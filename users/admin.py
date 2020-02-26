from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model=Profile
    list_display=['user','image','city','tc','soyad','tel','maas_banka','kredi_tutari','kredi_talebi','join_date','updated_date','ad']
    list_display_links = list_display
    search_fields = list_display
    list_filter=['city','join_date']
