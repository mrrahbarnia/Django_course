from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    captcha = CaptchaField()


class LoginForm(AuthenticationForm):
    pass
    # email = forms.EmailField(max_length=100,required=False)

class ForgotForm(forms.Form):
    email = forms.EmailField(max_length=100)