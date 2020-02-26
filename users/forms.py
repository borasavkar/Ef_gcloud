from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    # username = forms.CharField(max_length="10")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı Adınız'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Adresiniz'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Parolanız'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Parolanızı Tekrar Giriniz'}),
        }
class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı Adınız'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Adresiniz'}),
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','tc','ad','soyad','tel','maas_banka','kredi_tutari','kredi_talebi','city']
        widgets = {
            'tc': forms.NumberInput(attrs={'placeholder': 'Tc Numaranız','id':'tc_input'}),
            'ad': forms.TextInput(attrs={'placeholder': 'Adınız','id':'ad_input'}),
            'soyad': forms.TextInput(attrs={'placeholder': 'Soyadınız'}),
            'tel': forms.NumberInput(attrs={'placeholder': '(05__) ___ __ __','id':'tel'}),
            # 'maas_banka': forms.TextInput(attrs={'placeholder': 'Maaş Aldığınız Banka'}),
            # 'kredi_tutari': forms.NumberInput(attrs={'placeholder': 'Maaşınızı Aldığınız Bankadaki Kredi Tutarınız'}),
            # 'kredi_talebi': forms.NumberInput(attrs={'placeholder': 'Ne Kadar Krediye İhtiyacınız var?'}),
        }
        labels = {
            'ad' : 'Adınız',
            'soyad' : 'Soyadınız',
            'tc': 'T.C. No.',
            'tel' : 'Telefon Numaranız',
            'maas_banka' : 'Maaş Aldığınız Banka',
            'kredi_tutari' : 'Varsa Maaş Aldığınız Bankadaki Kredi Tutarı',
            'kredi_talebi' : 'Kredi Talebiniz',
            'city' : 'Şehir'
        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı adınız'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Parolanız'}),
        }