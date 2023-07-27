from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.form import SignupForm



# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,f'Welcome {request.user.username}')
                    return redirect("/")
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
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
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.success(request,f"Welcome {request.user.username}")
                return redirect("/")
        else:
            form = SignupForm()
    else:
        messages.info(request,f'You have already signed up as {request.user.username}')
        return redirect("/")
    context = {'form':form}
    return render(request,'accounts/signup.html',context)
        