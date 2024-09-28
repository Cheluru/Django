from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app1.models import *

# Create your views here.
def feed(request):
    res=tweeter.objects.all()[::-1]
    return render(request,'feed.html',{'data':res})

def loginView(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=="POST":
        u=request.POST.get('usern')
        p=request.POST.get('passw')
        result = authenticate(request,username=u,password=p)

        if result is not None:
            login(request,result)   
            return redirect('profile') 
        else:
            return render(request,'login.html')                      
    return render(request,'login.html')


def userExists(x):
    if User.objects.filter(username=x).exists():
        return True
    else:
        return False
    
def length(z):
    if len(z)>8:return True
    else:return False

def spaceExists(y):
    if len(y.split())>1:
        return True
    else:
        return False
    
def checkPass(a):
    if len(a)>8:return True
    else:return False

def isSpl(b):
    if b.isalnum():
        return False
    else:return True

def register(request):
    if request.method=="POST":
        u=request.POST.get('usern')    
        f=request.POST.get('fname')    
        l=request.POST.get('lname')    
        m=request.POST.get('mail')    
        p=request.POST.get('passw')
        print(u,f,l,m,p)

        if userExists(u):
            d={'warn':"Arey Thamudu alreadt username taken !"}
            return render(request,'register.html',d)
        if not length(u):
            d={'warn':"Username should graterthan 8"}
            return render(request,'register.html',d)
        
        if spaceExists(u):
            d={'warn':"Username should not contain spaces"}
            return render(request,'register.html',d)
        
        if not checkPass(p):
            d={'warn':"Password should atleast 8 characters"}
            return render(request,'register.html',d)
        
        if not isSpl(p):
            d={'warn':"You havnt used special character"}
            return render(request,'register.html',d)
        
        obj=User.objects.create_user(
            username=u,
            first_name=f,
            last_name=l,
            email=m,
            password=p
            )
        obj.save()

    return render(request,'register.html')

@login_required(login_url='login')
def postView(request):
    if request.method=="POST":
        t=request.POST.get('title')
        c=request.POST.get('cap')
        u=request.user.username
        obj=tweeter(person=u,title=t,caption=c)
        obj.save()
    return render(request,'post.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

def logoutView(request):
    logout(request)
    return redirect('login')


def onepost(request,rid):
    res=tweeter.objects.get(id=rid)
    return render(request,'postdyn.html',{'data':res})


def dele(request,rid):
    obj=tweeter.objects.get(id=rid)
    obj.delete()
    return redirect('home')


@login_required(login_url='login')
def manufact(request):
    if request.method=="POST":
        b=request.POST.get('br')
        c=request.POST.get('co')
        t=request.POST.get('to')
        obj=Manufacturer(brand=b,ceo=c,turnover=t)
        obj.save()
    return render(request,'manufac.html')

def car(request):
    if request.method='POST':
        c=request.POST.get('cn')
        y=request.POST.get('yor')
        m=request.POST.get('mid')
        if Manufacturer.objects.filter(id=m).exists():
            mn=Manufacturer.objects.get(id=m)
            f=request.POST.get('fu')
            obj=Car(name=c,year=y,manufacture=mn,fuel=f)
            obj.save()
    return render(request,'display.html')

def showcars(request):
    obj1=Car.objects.all()[::-1]
    if request.method=="POSt":
        b=request.POST.get('brand')
        obj1=Car.objects.filter(name_icontains=b)
    return render(request,'car.html')

def update(request,rid):
    obj=tweeter.objects.get(id=rid)

    if request.method="POST":
        t=request.POST.get('title')
        c=request.POST.get('cap')
        o=tweeter.objects.get(id=rid)
        o.title=t
        o.caption=c
        o.save()
        return redirect('home')