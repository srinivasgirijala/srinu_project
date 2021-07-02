
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import Newuser,Appli
# Create your views here.

def careers(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        state=request.POST['state']
        address=request.POST['address']
        Gender=request.POST['Gender']
        location=request.POST['location']
        skills=request.POST['skills']
        textarea=request.POST['textarea']
        User=Appli(firstname=firstname,lastname=lastname,phonenumber=phonenumber,email=email,state=state,address=address,Gender=Gender,location=location,skills=skills,textarea=textarea)
        User.save()
        messages.success(request,'The Application of' + request.POST ['firstname']  +   "Successfully Done")
        return redirect('/')
    else:
     return render(request,'careers.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        phonenumber=request.POST['phonenumber']
        user=Newuser(username=username,email=email,password=password,phonenumber=phonenumber)
        user.save()
        messages.success(request,'The New User' + request.POST ['username']  +   "Successfully Done")
        return render(request,'login.html')
    else:
     return render(request,'register.html')

def login(request):
    if request.method=='POST':
        try:
            Userdetails=Newuser.objects.get(email=request.POST['email'],password=request.POST['password'])
            print('email',Userdetails)
            request.session['email']=Userdetails.email
            return redirect('/')
        except Newuser.DoesNotExist as e:
            messages.success(request,'email/password invalid')
    return render(request,'login.html')

def logout(request):
    try:
     del request.session['email']
    except:
        return redirect('/')
    return redirect('/')


def contact(request):
    return render(request,'contact.html')


def About(request):
    return render(request,'About.html')

def created(request):
    return render(request,'created.html')
    
def become(request):
    return render(request,'become.html')
    
def training(request):
    return render(request,'training.html')
    
def technologies(request):
    return render(request,'technologies.html')