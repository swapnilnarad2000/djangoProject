# import models here
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    # context = {
    #     'var1' : "hi",
    #     'var2' : "bye"
    # }
    return render(request,'index.html')
    # return HttpResponse('Hi your server is active')
def about(request):
    return render(request,'about.html')

def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name , email = email,phone=phone,desc = desc,date = datetime.now())
        contact.save()
        messages.success(request, 'Review added successfully')
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')
