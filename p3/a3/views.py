from django.shortcuts import render,redirect, get_object_or_404
from .models import Leaves , Salary , Profile , Assign_sub , Feedback , Syl_updates
from django.http import HttpResponse
from django.core.mail import send_mail
from.import forms
from accounts.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"home.html")

def hr_home(request):
    return render(request,"hr_home.html")

def hod_home(request):
    return render(request,"hod_home.html")

def emp_home(request):
        return render(request,"emp_home.html")

def hr_nav(request):
    return render(request,"hr_nav.html")

def nav_bar(request):
    return render(request,"nav_bar.html")

def feedback(request):
    employee = User.objects.all().order_by("pk")
    return render(request,"feedback.html",{"employee":employee})

def feedbackform(request):
    if request.method == "POST":
        print("auth")
        form = forms.Feedback(request.POST)
        form.request = request
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                return HttpResponse(e)
            return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../emp_home'><button>Goto Home</button></a>")
        else:
            form = forms.Feedback()
        return render(request,"feedbackform.html",{'form':form})
    else:
        print("failed")
        form = Feedback()
    return render(request,"feedbackform.html")

def delete_view(request,id):
    user = User.objects.get(pk=id)
    email = User.objects.get("email")
    user.delete()
    subject = 'FROM HR MANAGEMENT'
    message = 'YOUR REQUEST IS REJECTED PLEASE CONTACT ADMINISTRATION'
    from_email = 'gvpcehr123@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect(reverse("a3:update_employees"))

def delete_v(request,id):
    user = Profile.objects.get(pk=id)
    user.delete()
    return redirect(reverse("a3:employees"))

def delete_z(request,id):
    user = Leaves.objects.get(pk=id)
    email = user.email
    user.delete()
    subject = 'ABOUT LEAVES'
    message = 'YOUR LEAVE REQUEST IS REJECTED'
    from_email = 'gvpcehr123@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect(reverse("a3:leaves_report"))

def accept_view(request,id):
    user = User.objects.get(pk = id)
    # user.delete().
    user.is_active = True
    email = user.email 
    user.save()
    #send mails
    subject = 'FROM HR MANAGEMENT'
    message = 'YOU ARE VERIFIED BY HR PLEASE LOGIN KNOW'
    from_email = 'gvpcehr123@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect(reverse("a3:update_employees"))

def accept_leaves(request,id):
    user = Leaves.objects.get(pk = id)
    user.delete()
    email = user.email 
    user.save()
    #send mails
    subject = 'FROM HR MANAGEMENT'
    message = 'YOUR LEAVE REQUEST IS ACCEPTED'
    from_email = 'gvpcehr123@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect(reverse("a3:update_employees"))

def assign_sub(request):
    if request.method == "POST":
        print("auth")
        form = forms.Assign_sub(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../hr_home'><button>Goto Home</button></a>")
            except Exception:
                return HttpResponse('<body style="background-color: #f8f8f8;  color: #333;  border: 2px solid #ccc;  padding: 20px;  border-radius: 6px;  text-align: center;  max-width: 400px;  margin: 0 auto; font-size: 40px;  display: block;  margin-bottom: 20px;}">Oops, something went wrong</body>')
        else:
            form = forms.Assign_sub()
        return render(request,"assign_sub.html",{'form':form})
    else:
        print("failed")
        form = Assign_sub()
    return render(request,"assign_sub.html")

def emp_profile(request):
    username = request.user.username
    profile = Profile.objects.filter(username = username).first()
    context={
        "profile" : profile
    }
    return render(request,"emp_profile.html",context)

def hod_profile(request):
    username = request.user.username
    profile = Profile.objects.filter(username = username).first()
    context={
        "profile" : profile
    }
    return render(request,"hod_profile.html",context)

def emp_nav(request):
    return render(request,"emp_nav.html")

def profile(request):
    if request.method == "POST":
        print("auth")
        form = forms.Profile( request.POST,)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../user_login'><button>Goto Home</button></a>")
            except Exception:
                return HttpResponse("<p style='color:green; font-size:40px;'>user does not exist")

        else:
            return redirect('a3:profile')
    else:            
        print("failed")
    return render(request,"profile.html")


def employees(request):
    # employee = User.objects.filter(employee_status = "employee")
    employee = Profile.objects.all().order_by("pk")
    return render(request,"employees.html",{"employee":employee})

def syllabus(request):
    # employee = User.objects.filter(employee_status = "employee")
    syllabus = Syl_updates.objects.all().order_by("pk")
    return render(request,"syllabus.html",{"syllabus":syllabus})

def update_employees(request):
    # employee = User.objects.filter(employee_status = "employee")
    employee = User.objects.filter(is_active=False).order_by("pk")
    return render(request,"update_employees.html",{"update_employee":employee})

def add_salary(request):
    if request.method == "POST":
        print("auth")
        form = forms.Salary(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../hr_home'><button>Goto Home</button></a>")
            except Exception:
                return HttpResponse("<p style='color:green; font-size:40px;'>user does not exist")
    else:
        form= Salary()
    return render(request,"add_salary.html")



def salary_updates(request):
    username = request.user.username
    #user = User.objects.get(username=username)
    #salary = user.salary
    salary= Salary.objects.filter(username = username).first()
    context ={
        "salary":salary,
        #"user" : user
    }
    return render(request,"salary_updates.html",context)

def sal_details(request):
    salary= Salary.objects.all().order_by("date")
    return render(request,"sal_details.html", {"salary":salary})

def sub_details(request):
    subjects= Assign_sub.objects.all().order_by("emp_id")
    return render(request,"sub_details.html", {"subjects":subjects})

def sub_updates(request):
    username = request.user.username
    subject= Assign_sub.objects.filter(name = username).first()
    return render(request,"sub_updates.html", {"subject":subject})

def syl_updates(request):
    if request.method == "POST":
        print("auth")
        form = forms.Syl_updates(request.POST)
        if form.is_valid():
            print("saved")
            try:
                form.save()
                return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../emp_home'><button>Goto Home</button></a>")
            except Exception:
                return HttpResponse(" <p style='color:green; font-size:40px;'>user does not exist")
        else:
            HttpResponse("form is not valid")
    else:
        print("failed")
        form= Syl_updates()
    print("end")
    return render(request,"syl_updates.html")

# @login_required(login_url = "/login")
def leaves(request):
    if request.method == 'POST':
        form =forms.Leaves(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../emp_home'><button>Goto Home</button></a>")
            except Exception:
                return HttpResponse('<p style="color:green; font-size:40px;">user does not exist</p>')
    else:
        form = Leaves()
    return render(request, 'leaves.html', {'form': form})

def leaves_report(request):
    leaves= Leaves.objects.all().order_by("startdate")
    return render(request,"leaves_report.html", {"leaves":leaves},)