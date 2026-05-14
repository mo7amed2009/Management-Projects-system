from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.decorators import user_passes_test,login_required,login_not_required
from django.views import View 
from django.views.generic import *
# Create your views here.

@login_not_required
def signup_view(request):
    if request.method =='POST':    # To Save In Date Base
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('all_projects')
    else:                           # To Show In Template
        form=UserForm()
    return render(request,'accounts/signup.html',{'form':form})
@login_required    
def logout_view(request):
    logout(request)
    return redirect('all_projects')

login_required   
def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form=ProfileForm(request.POST,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('all_projects')
    
    else:
        user_form = UserForm( instance=request.user)
        profile_form=ProfileForm(instance=profile)
    context={
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request,'accounts/edit_profile.html',context)
@login_required
def my_profile(request):
    
    profile=Profile.objects.get(user=request.user)
    
    user=User.objects.get(id=request.user.id)

    context={
        'profile':profile,
        'user':user
    }
    return render(request,'accounts/my_profile.html',context)

@login_required
def show_profile(request,profile_id):
    profile=Profile.objects.get(id=profile_id)

    return render(request,'accounts/show_profile.html',{'profile':profile})

