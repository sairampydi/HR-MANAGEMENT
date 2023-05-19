from django.shortcuts import render,redirect, get_object_or_404
from .models import Leaves , Salary , Profile , Assign_sub
from django.http import HttpResponse
# from .forms import Leaves
from.import forms
from accounts.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"home.html")

def hr_home(request):
    return render(request,"hr_home.html")

def emp_home(request):
    # profile = Profile.objects.all()
    # user = User.objects.all()
    # if(profile.username == user.username):
        return render(request,"emp_home.html")
    # else:
    #     return redirect("emp_home")
    

def hr_nav(request):
    return render(request,"hr_nav.html")

def nav_bar(request):
    return render(request,"nav_bar.html")

def delete_view(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect(reverse("a3:employees"))

def assign_sub(request):
    if request.method == "POST":
        print("auth")
        form = forms.Assign_sub(request.POST)
        if form.is_valid():
            print("saved")
            form.save()
            return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../hr_home'><button>Goto Home</button></a>")
        else:
            form = forms.Assign_sub()
        return render(request,"assign_sub.html",{'form':form})
    else:
        print("failed")
        form = Assign_sub()
    return render(request,"assign_sub.html")

def emp_nav(request):
    return render(request,"emp_nav.html")

def profile(request):
    if request.method == "POST":
        print("auth")
        form = forms.Profile( request.POST,)
        if form.is_valid():
            print("saved")
            form.save()
            return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../user_login'><button>Goto Home</button></a>")
        else:
            return redirect('a3:profile')
    else:
        print("failed")
        #form= Profile()
    return render(request,"profile.html")


def employees(request):
    # employee = User.objects.filter(employee_status = "employee")
    employee = Profile.objects.all().order_by("pk")
    return render(request,"employees.html",{"employee":employee})

def update_employees(request):
    # employee = User.objects.filter(employee_status = "employee")
    employee = User.objects.all().order_by("pk")
    return render(request,"update_employees.html",{"update_employee":employee})

def add_salary(request):
    if request.method == "POST":
        print("auth")
        form = forms.Salary(request.POST)
        if form.is_valid():
            print("saved")
            form.save()
            return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../hr_home'><button>goto home</button></a>")
        else:
            return HttpResponse("form is not vallid")
    else:
        print("failed")
        form= Salary()
    return render(request,"add_salary.html")

def leaves_report(request):
    leaves= Leaves.objects.all().order_by("startdate")
    return render(request,"leaves_report.html", {"leaves":leaves},)

def salary_updates(request):
    username = request.user.username
    #user = User.objects.get(username=username)
    #salary = user.salary
    salary= Salary.objects.filter(username = username)
    context ={
        "salary":salary,
        #"user" : user
    }
    return render(request,"salary_updates.html",context)

def sal_details(request):
    salary= Salary.objects.all().order_by("date")
    return render(request,"sal_details.html", {"salary":salary})

def sub_updates(request):
    subject= Assign_sub.objects.all().order_by("name")
    return render(request,"sub_updates.html", {"subject":subject})

# @login_required(login_url = "/login")
def leaves(request):
    if request.method == 'POST':
        form =forms.Leaves(request.POST)
        if form.is_valid():
            form.save()
            return redirect("a3:home")
    else:
        form = Leaves()
    return render(request, 'leaves.html', {'form': form})

