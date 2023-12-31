from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from captcha.fields import CaptchaField
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
    username = forms.CharField(min_length=5, max_length=50, validators= [RegexValidator(r"^(?=[a-zA-Z0-9._]{5,20}$)(?!.*[_.]{2})[^_.].*[^_.]$",
                        message="The username is 8-20 characters long and must include numbers and words.")], widget=forms.TextInput(attrs={"placeholder":"Enter your username"}))
    email = forms.EmailField(min_length=6, max_length=50, validators=[RegexValidator(r'^[A-Za-z0-9+_.-]+@(.+)$',
                            message="The email format is not correct.")], widget=forms.TextInput(attrs={"placeholder":"Example: admin@admin.com"}))
    password1 = forms.CharField(label="Password", min_length=3, max_length=50, widget=forms.PasswordInput(attrs={"placeholder":"Enter you password"}))
    password2 = forms.CharField(label="Password Confirmation", min_length=3, max_length=50, widget=forms.PasswordInput(attrs={"placeholder":"Enter the same password as before"}))
    captcha = CaptchaField(label="Please resolve this simple math challenge to prove your not a robot")
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username', widget=forms.TextInput(attrs={"placeholder":"Enter either your username or email"}))
    password = forms.CharField(label="Password", min_length=3, max_length=50, widget=forms.PasswordInput(attrs={"placeholder":"Enter you password"}))
    