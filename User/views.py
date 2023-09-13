from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import Profile
from .forms import SignupForm ,UserActiveForm
from django.core.mail import send_mail

# Create your views here.


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save(commit=False)
            myform.active = False
            myform.save()
            profile = Profile.objects.get(user__username=username)
            print(profile)
            print(profile.code)
            send_mail(
                        subject= 'Active your Account',
                        message= f'This code {profile.code} for activate your account',
                        from_email = 'aymanabdelfattahm@gmail.com',
                        recipient_list = [email],
                        fail_silently=False,)
            return redirect(f'/accounts/{username}/activate')

       
    else :
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})

def user_activate(request,username):
    profile = Profile.objects.get(user__username = username)
    if request.method == 'POST':
        form = UserActiveForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code :
                profile.code_used = True
                profile.save()
                return redirect('/accounts/login')
    
    else:
        form = UserActiveForm()
    return render(request,"registration/activate.html",{'form':form})
    
