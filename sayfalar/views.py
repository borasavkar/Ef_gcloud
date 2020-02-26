from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post,Basvuru
from .forms import KrediBasvuruForm,MesajForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

def home(request):
    kredi_form = KrediBasvuruForm()
    krediBasvurusu(request)
    return render(request,"sayfalar/index.html",{'title':'Emekliye Kredi','kredi_form':kredi_form})
def about(request):
    kredi_form = KrediBasvuruForm()
    krediBasvurusu(request)
    return render(request, "sayfalar/about.html", {'title':'Hakkımızda','kredi_form':kredi_form})
def contact(request):
    kredi_form = KrediBasvuruForm()
    krediBasvurusu(request)
    contact_form = MesajForm()
    if request.method=='POST':
        contact_form=MesajForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, f'Mesajınızı Aldık. İlginiz İçin Teşekkürler')
            ad=contact_form.cleaned_data.get('ad')
            soyad=contact_form.cleaned_data.get('soyad')
            tel=contact_form.cleaned_data.get('tel')
            email=contact_form.cleaned_data.get('email')
            mesaj=contact_form.cleaned_data.get('mesaj')
            mesaj_tarihi=contact_form.instance.date_posted
            subject=f'''Yeni Mesaj - {ad} {soyad} {tel} {email}'''
            contact_mail_body=f'''
            Ad: {ad}
            Soyad: {soyad}
            Tel: {tel}
            Email: {email}
            Mesaj: {mesaj}
            Mesaj Tarihi: {mesaj_tarihi}
            '''
            contact_mail_body_html=f'''
            <div style="font-size:30px">
            <strong style="color:#e8491d">Ad:</strong> {ad}<br>
            <strong style="color:#e8491d">Soyad:</strong> {soyad}<br>
            <strong style="color:#e8491d">Tel:</strong> <a href="tel:{tel}"> {tel}</a><br>
            <strong style="color:#e8491d">Email:</strong> <a href="mailto:{email}">{email}</a><br>
            <strong style="color:#e8491d">Mesaj:</strong> {mesaj}<br>
            <strong style="color:#e8491d">Mesaj Tarihi:</strong> {mesaj_tarihi}<br>
            <h1 style="margin-top:50px;text-align: center;"><strong style="color:#e8491d">Emekli</strong>Finans<span class="sup">&reg;</span></h1>
            </div>
            '''
            sender='borasavkar@gmail.com'
            recipient_list=['borasavkar@hotmail.com']
            mail=EmailMultiAlternatives(subject,contact_mail_body,sender,recipient_list)
            mail.attach_alternative(contact_mail_body_html,"text/html")
            mail.send()
            return redirect('home')
    else:
        contact_form = MesajForm()
    return render(request, "sayfalar/contact.html", {'kredi_form':kredi_form,'contact_form':contact_form,'title':'Bize Ulaşın'})
def basvuru(request):
    kredi_form = KrediBasvuruForm()
    krediBasvurusu(request)
    return render(request, "sayfalar/basvuru.html", {'kredi_form':kredi_form,'title':'Kredi Başvurusu'})
def EmekliyeKredi(request):
    kredi_form = KrediBasvuruForm()
    krediBasvurusu(request)
    return render(request, "sayfalar/EmekliyeKredi.html", {'kredi_form':kredi_form,'title':'Emekliye Kredi'})
def ptt_kredi(request):
    kredi_form = KrediBasvuruForm()
    krediBasvurusu(request)
    return render(request, "sayfalar/ptt_kredi.html", {'kredi_form':kredi_form,'title':'Ptt Kredi'})
def SicilBozuk(request):
    kredi_form = KrediBasvuruForm()
    krediBasvurusu(request)
    return render(request, "sayfalar/SicilBozuk.html", {'kredi_form':kredi_form,'title':'Sicili Bozuk'})
def kisisel(request):
    return render(request, "sayfalar/Docs/Documents/KisiselVerilerinKorunmasi.pdf", {})
def posts(request):
    context={
        'posts':Post.objects.all(),
        'title':'Yorumlar',
    }
    return render(request,'sayfalar/posts.html',context)
def login(request):
    return render(request,'login.html',{'title':'Giriş'})
def logout(request):
    return render(request,'logout.html',{'title':'Çıkış'})
# def register(request):
#     return render(request,'register.html',{'title':'Kayıt Ol'})
class PostListView(ListView):
    kredi_form = KrediBasvuruForm()
    'kredi'
    model = Post
    template_name='sayfalar/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name='sayfalar/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name='sayfalar/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        post = form.cleaned_data.get('content')
        author = form.instance.author
        post_date = form.instance.date_posted
        subject=f'''YENİ YORUM: {post} YORUM YAPAN: {author}'''
        message_body=f'''
        YORUM YAPAN: {author}
        YORUMU: {post}
        YORUM TARİHİ: {post_date}
        '''
        message_body_html=f'''
        <div style="font-size:30px">
        <strong style="color:#e8491d">YORUM YAPAN:</strong> {author}<br>
        <strong style="color:#e8491d">YORUMU:</strong> {post}<br>
        <strong style="color:#e8491d">YORUM TARİHİ:</strong> {post_date}
        </div>
        '''
        sender='borasavkar@gmail.com'
        recipient_list=['borasavkar@hotmail.com']
        # send_mail(subject,message_body,sender,recipient_list,fail_silently=False,)
        email=EmailMultiAlternatives(subject,message_body,sender,recipient_list)
        email.attach_alternative(message_body_html,"text/html")
        email.send()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/posts'
    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False
def krediBasvurusu(request):
    kredi_form = KrediBasvuruForm()
    if request.method=='POST':
        kredi_form=KrediBasvuruForm(request.POST)
        if kredi_form.is_valid():
            kredi_form.save()
            messages.success(request, f'Kredi Başvuru Formunuz Başarı ile Bize Ulaştı.')
            ad=kredi_form.cleaned_data.get('ad')
            soyad=kredi_form.cleaned_data.get('soyad')
            tel=kredi_form.cleaned_data.get('tel')
            maas_banka=kredi_form.cleaned_data.get('maas_banka')
            kredi_tutari=kredi_form.cleaned_data.get('kredi_tutari')
            kredi_talebi=kredi_form.cleaned_data.get('kredi_talebi')
            city=kredi_form.cleaned_data.get('city')
            basvuru_tarihi=kredi_form.instance.date_posted
            subject=f'''{ad} {soyad} {tel} {maas_banka} Mevcut Kredi: {kredi_tutari} Kredi Talebi: {kredi_talebi} {city}'''
            message_body=f'''
            Ad: {ad}
            Soyad: {soyad}
            Tel: {tel}
            Maaş Bankası: {maas_banka}
            Mevcut Kredi: {kredi_tutari}
            Kredi Talebi: {kredi_talebi}
            Şehir: {city}
            Başvuru Tarihi: {basvuru_tarihi}'''
            message_body_html=f'''
            <div style="font-size:30px">
            <strong style="color:#e8491d">Ad:</strong> {ad}<br>
            <strong style="color:#e8491d">Soyad:</strong> {soyad}<br>
            <strong style="color:#e8491d">Tel:</strong> <a href="tel:{tel}"> {tel}</a><br>
            <strong style="color:#e8491d">Maaş Bankası:</strong> {maas_banka}<br>
            <strong style="color:#e8491d">Mevcut Kredi:</strong> {kredi_tutari}<br>
            <strong style="color:#e8491d">Kredi Talebi:</strong> {kredi_talebi}<br>
            <strong style="color:#e8491d">Şehir:</strong> {city}<br>
            <strong style="color:#e8491d">Başvuru Tarihi:</strong> {basvuru_tarihi}<br>
            <h1 style="margin-top:50px;text-align: center;"><strong style="color:#e8491d">Emekli</strong>Finans<span class="sup">&reg;</span></h1>
            </div>
            '''
            sender='borasavkar@gmail.com'
            recipient_list=['borasavkar@hotmail.com']
            # send_mail(subject,message_body,sender,recipient_list,fail_silently=False,)
            email=EmailMultiAlternatives(subject,message_body,sender,recipient_list)
            email.attach_alternative(message_body_html,"text/html")
            email.send()
            return redirect('home')
        else:
            # messages.warning(request, f'Form Gönderimi Başarısız Oldu. Lütfen Tekrar Deneyiniz...')
            kredi_form = KrediBasvuruForm()
    else:
        kredi_form = KrediBasvuruForm()






