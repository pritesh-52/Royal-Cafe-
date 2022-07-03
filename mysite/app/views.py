from django.shortcuts import render,redirect
from  django.http import  HttpResponse
from .models import  *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request,'index.html')


def insert(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    guests=request.POST['guests']
    dob=request.POST['date']
    time=request.POST['time']
    message=request.POST['message']

    newtable=Book.objects.create(name=name,email=email,phone=phone,guest=guests,dob=dob,
                                 time=time,message=message)

    messages.success(request, 'Your request has been accepted.')

    return render(request,'index.html')

def admin(request):

    all_data=Book.objects.all()
    return render(request,'admin.html',{'key':all_data})


def conformpage(request,pk):
    getdata = Book.objects.get(id=pk)
    return  render(request,'conform.html',{'key1':getdata})
def accepted(request,pk):
    getdata = Book.objects.get(id=pk)
    email=request.POST['email']
    dob=request.POST['dob']
    send_mail(
        'Royal Cafe',
        f'Hey Your table has been booked on Date {dob}',
        'priteshbhatiya52@gmail.com',
        [email],
        fail_silently=False,
    )
    return render(request,'show.html',{'key2':getdata})

def rejected(request,pk):
    deletedata=Book.objects.get(id=pk)
    deletedata.delete()
    return redirect('admin')

def signinpage(request):
    return render(request,'signin.html')

def usersignin(request):
    uname=request.POST['uname']
    password=request.POST['password']

    us=signin.objects.get(uname=uname,password=password)

    if us.uname=="admin" and us.password=="1234":
        return render(request,'admin.html')
    else:
        print("Passoword does not match")

def showpage(request):
    return render(request,'show.html')












# Create your views here.
