from django import forms
from website.models import Newslettter
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
    
class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newslettter
        fields = "__all__"


