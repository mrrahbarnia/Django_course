from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your message submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,"your message didnt submit...try again")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def news_letter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"your Email address was sent")
            return HttpResponseRedirect("/")
        else:
            messages.add_message(request,messages.ERROR,"your Email address was not sent...try again")
    form = NewsletterForm()
    return render(request,"website/contact.html",{"form":form})

