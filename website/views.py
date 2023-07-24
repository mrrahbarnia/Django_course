from django.shortcuts import render,HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            i = Contact()
            i.name = "Unknown"
            i.email = form.cleaned_data['email']
            i.subject = form.cleaned_data['subject']
            i.message = form.cleaned_data['message']
            i.save()
            messages.success(request,'Your message submitted successfully')
        else:
            messages.error(request,"Your message didn't submit")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def news_letter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"your Email address was sent")
            return HttpResponseRedirect("/")
    form = NewsletterForm()
    return render(request,"website/contact.html",{"form":form})

