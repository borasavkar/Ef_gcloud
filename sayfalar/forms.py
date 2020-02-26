from django import forms
from .models import Basvuru,Mesaj
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.layout import Field

class kvk_confirm(Field):
    template = 'sayfalar/includes/custom_checkbox.html'

class KrediBasvuruForm(forms.ModelForm):
    kvk_confirm = forms.BooleanField(required=True,label='Kişisel Verilerin Korunması Kanunu hakkında bilgilendirmeyi okudum, kabul ediyorum.')
    kvk_confirm.widget.attrs.update({'id':'kvk_checkbox'})
    class Meta:
        model = Basvuru
        fields = ('tc','ad','soyad','tel','maas_banka','kredi_tutari','kredi_talebi','city','kvk_confirm')
        widgets = {
            'tc': forms.NumberInput(attrs={'placeholder': 'Tc Numaranız','id':'tc_input'}),
            'ad': forms.TextInput(attrs={'placeholder': 'Adınız','id':'ad_input'}),
            'soyad': forms.TextInput(attrs={'placeholder': 'Soyadınız'}),
            'tel': forms.NumberInput(attrs={'placeholder': '(05__) ___ __ __','id':'tel'}),
            'kvk_confirm' : forms.BooleanField()
            # 'maas_banka': forms.TextInput(attrs={'placeholder': 'Maaş Aldığınız Banka'}),
            # 'kredi_tutari': forms.NumberInput(attrs={'placeholder': 'Maaşınızı Aldığınız Bankadaki Kredi Tutarınız'}),
            # 'kredi_talebi': forms.NumberInput(attrs={'placeholder': 'Ne Kadar Krediye İhtiyacınız var?'}),
        }
        labels = {
            'ad' : 'Adınız',
            'soyad' : 'Soyadınız',
            'tc': 'T.C. No.',
            'tel' : 'Telefon Numaranız',
            'maas_banka' : 'Maaşınızı Aldığınız Banka',
            'kredi_tutari' : 'Varsa Maaş Aldığınız Bankadaki Kredi Tutarı',
            'kredi_talebi' : 'Kredi Talebiniz',
            'city' : 'Şehir'
        }
        # help_text = {
        #     'tc':'Lütfen T.C. Kimlik Numarınızı Girin...'
        # }
        # validators = {
        #     'tc' : 'tc_validate',
        #     'tel' : 'phone_regex'
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('ad', css_class='form-group col-md-6 mb-0'),
    #             Column('soyad', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('tc', css_class='form-group col-md-6 mb-0'),
    #             Column('tel', css_class='form-group col-md-6 mb-0',css_id="tel"),
    #             css_class='form-row'
    #         ),
    #         'maas_banka',
    #         'kredi_tutari',
    #         'kredi_talebi',
    #         'city',
    #         kvk_confirm('Kişisel Verilerin Korunması Kanunu hakkında bilgilendirmeyi okudum, kabul ediyorum.'),
    #         Submit('submit','Başvur')
    #     )

class MesajForm(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields= ('ad', 'soyad', 'tel', 'email', 'mesaj')
        widgets = {
            'ad': forms.TextInput(attrs={'placeholder': 'Adınız'}),
            'soyad': forms.TextInput(attrs={'placeholder': 'Soyadınız'}),
            'tel': forms.NumberInput(attrs={'placeholder': 'Telefon Numarınız'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-Posta'}),
            'mesaj': forms.Textarea(attrs={'placeholder':'Mesajınız','rows':5}),
        }
        labels = {
            'ad' : 'Adınız',
            'soyad' : 'Soyadınız',
            'tel' : 'Telefon Numaranız',
        }
