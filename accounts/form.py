from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    captcha = CaptchaField()