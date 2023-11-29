from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django .contrib.auth import authenticate,login,logout ,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def login_form(request):
    if request.method =='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('logouta')
            else:
                messages.error(request,'Invalid password')
        else:
                messages.error(request,'Invalid password')
    else:
         form=AuthenticationForm()
    return render(request,'login.html', {'form':form })


def logout_form(request):
     return render(request,'logout.html')
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')  


def signup_form(request):
    if request.method=='POST':
         form=SignUpForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('login')
         
    else:
         form=SignUpForm
    return render(request,'signup.html',{'form':form})



def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password changes successfull')
            return redirect('login')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request, 'changepass.html',{'form':form})

