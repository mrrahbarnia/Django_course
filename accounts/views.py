from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.form import SignupForm,LoginForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,f'Welcome {request.user.username}')
                    return redirect("/")
            else:
                messages.error(request,"The information must be valid.")
                return redirect("/")
        return render(request,'accounts/login.html',{"form":LoginForm()})
    else:
        messages.info(request,f"You have already logged in as {request.user.username}")
        return redirect("/")
        


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'logged out')
        return redirect("/")
    else:
        return HttpResponseRedirect(reverse('accounts:login'))



def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Welcome")
                return HttpResponseRedirect(reverse('accounts:login'))
            else:
                messages.error(request,"The information must be valid.")
                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            return render(request, 'accounts/signup.html', {"form":SignupForm()})
    else:
        messages.info(request,f'You have already signed up as {request.user.username}')
        return redirect("/")