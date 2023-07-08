from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.views.decorators.cache import never_cache
from accounts.forms import Userform
import random
from django.urls import reverse
# Create your views here.
s = set()
def signup_views(request):
    if request.method == 'POST':
        form = Userform(request.POST,request.FILES)
        if form.is_valid():
            print("signed up")
            while True:
                a=random.randint(1000,9999)
                if a not in s:
                    s.add(a)
                    b=a
                    print("B value:",b)
                    break
                else:
                    continue  
            form.save()
            #request.session['bar'] = a
            context = {
                'bar':b,
            }
            return render(request,"profile.html",context)
        else:
            print(form.errors)
        
    form = Userform
    return render(request,"signup.html",{'form':form})


@never_cache
def hr_login(request):
    if request.user.is_authenticated:
        print("auth")
        return redirect("a3:hr_home")  
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        u = User.objects.filter(username=username).first()
        if not u or u.employee_status != "hr":
            print("not HR")
            messages.success(request,"Incorrect Username or Password")
            return redirect("accounts:hr_login")
        user=authenticate(username=username,password=password)
        if user is not None:
            print("success")
            login(request,user)
            return redirect("a3:hr_home")
        else:
            print("failure")
            messages.success(request,"Incorrect Username or Password")
            return redirect("accounts:hr_login")
    else:
        form = AuthenticationForm()
    return render(request,'hr_login.html',{'form':form})


# @never_cache
def user_login(request):
    #user.objects.filter(employee_status = "employee")
    if request.user.is_authenticated:
        return redirect("a3:emp_home")  
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        u = User.objects.filter(username=username).first()
        if not u or u.employee_status != "employee"or u.position != "employee":
            messages.success(request,"Incorrect Username or Password")
            return redirect("accounts:user_login")
        if not u.is_active:
            return HttpResponse("style='border: 4px solid black; background: salmon'<i>&#9888;</i>your user is not yet accepted please contact administration")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("a3:emp_home")
        else:
            return HttpResponse("<p style='border: 1px solid darkred; background: salmon'><i>&#9888;</i>your username or password is worng try again</p>")
    else:
        form = AuthenticationForm()
    return render(request,'user_login.html',{'form':form})


def hod_login(request):
    #user.objects.filter(employee_status = "employee")
    if request.user.is_authenticated:
        return redirect("a3:hod_home")  
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        u = User.objects.filter(username=username).first()
        if not u or u.employee_status != "employee" or u.position != "hod":
            messages.success(request,"Incorrect Username or Password")
            return redirect("accounts:hod_login")
        if not u.is_active:
            return HttpResponse("<p style='font-size:50px;margin:20%; border: 4px solid black; background: salmon'><i>&#9888;</i>HR is not yet accepted please contact administration</p>")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("a3:hod_home")
        else:
            return HttpResponse("your username or password is worng try again")
    else:
        form = AuthenticationForm()
    return render(request,'hod_login.html',{'form':form})



def logout_views(request):
    logout(request)
    return redirect("a3:home")
    

def user_signup(request):
    return render(request,"user_signup.html")