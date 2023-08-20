from django.shortcuts import render,HttpResponse
from django.template import Context
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context={'var':'this is sent'}
    return render(request,'index.html',context)
    # return HttpResponse("<h1>This is Batman<h1>")
def service(request):
    return render(request,'service.html')
def help(request):
    return render(request,'help.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('text')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    
    return render(request,'contact.html')
