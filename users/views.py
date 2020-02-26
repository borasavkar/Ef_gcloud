from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,LoginForm
from sayfalar.models import Post,Basvuru
from sayfalar.forms import KrediBasvuruForm

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Tebrikler {username} kullanıcısı oluşturuldu!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form,'title':'Kayıt Ol'})
@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username=u_form.cleaned_data.get('username')
            messages.success(request, f'{username} kullanıcı profili güncellendi...')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
        'title':'Profil',
    }
    # return render(request,'users/profile.html',context,{'title':'Hesabım'})
    return render(request,'users/profile.html',context)
