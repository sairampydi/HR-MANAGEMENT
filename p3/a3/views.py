from django.shortcuts import render,redirect, get_object_or_404
from .models import Leaves , Salary ,Assign_sub,Profile , Feedback , Syl_updates
from django.http import HttpResponse
from django.core.mail import send_mail
from .import forms 
from .forms import Profile as  ProfileForm
from accounts.models import User
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def home(request):
    return render(request,"home.html")

def hr_home(request):
    return render(request,"hr_home.html")

def hod_home(request):
    username = request.user.username
    position = User.objects.filter(username = username).first() 
    return render(request,"hod_home.html",{"position":position})

def emp_home(request):
    username = request.user.username
    position = User.objects.filter(username = username).first()  
    return render(request,"emp_home.html",{"position":position})

def hr_nav(request):
    return render(request,"hr_nav.html")

def nav_bar(request):
    return render(request,"nav_bar.html")

def alert(request):
    return redirect("a3:feedbackform")

def feedback(request):
    user_stream = request.user.stream 
    
    employee = User.objects.all().order_by("pk")
    context ={
        "employee":employee,
        "user_stream" :user_stream
              }
    return render(request,"feedback.html",context)

def feedbackform(request):
    if request.method == "POST":
        print("auth")
        form = forms.Feedback(request.POST)
        form.request = request
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                context = {'exception_message': str(e)}
                return HttpResponse(render(request, 'alert.html', context))
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
    email = user.email
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
    users = User.objects.all()
    if request.method == "POST":
        print("auth")
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        section = request.POST.get('section')
        subject = request.POST.get('subject')

        # Perform form validation
        branchs = ["MCA", "EEE", "ECE", "CIVIL", "MECH", "CSE", "CSD", "CSM", "IT"]
        bb = branch.upper()
        if bb not in branchs:
            error_message = "Please select a correct branch."
            return HttpResponse(error_message)

        try:
            year = int(year)
        except ValueError:
            error_message = "Please enter a valid year."
            return HttpResponse(error_message)

        if year > 4:
            error_message = "Please enter a valid year."
            return HttpResponse(error_message)

        try:
            user = User.objects.get(username=name)
        except User.DoesNotExist:
            error_message = "User does not exist."
            return HttpResponse(error_message)

        try:
            temp = Assign_sub.objects.create(
                name=user,
                branch=branch,
                year=year,
                section=section,
                subject=subject,
                date=datetime.now()
            )
            return HttpResponse("<p style='color:green; font-size:40px;'>Successfully added</p> <a href='../hod_home'><button>Goto Home</button></a>")
        except Exception as e:
            return HttpResponse(str(e))
    else:
        form = Assign_sub()
    return render(request, "assign_sub.html", {'form': form, 'users': users})



def emp_profile(request):
    username = request.user.username
    position = request.user.position
    profile = Profile.objects.filter(username = username).first()
    context={
        "profile" : profile,
        "position":position
    }
    return render(request,"emp_profile.html",context)

def profile_view(request, username):
    profile = Profile.objects.get(username=username)
    context = {
        'profile': profile
    }
    
    return render(request, 'profile_view.html', context)



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
    if request.method == 'POST':
        # Retrieve data from the request
        username = request.user.username
        image = request.FILES.get('image')  
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        emp_id = request.POST.get('emp_id')
        dob = request.POST.get('dob')
        mobile = request.POST.get('mobile')
        department = request.POST.get('department')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        state = request.POST.get('state', 'None')
        education = request.POST.get('education', 'btech')
        experience = request.POST.get('experience', 'none')
        details = request.POST.get('details', 'none')
        postal_code = request.POST.get('postal_code', '12345')
        research = request.POST.get('research', 'None')

        profile = Profile(
            username = username,
            image=image,
            surname=surname,
            email=email,
            emp_id=emp_id,
            dob=dob,
            mobile=mobile,
            department = department,
            address=address,
            city=city,
            country=country,
            state=state,
            education=education,
            experience=experience,
            details=details,
            postal_code=postal_code,
            research=research
        )

        # Save the Profile object
        profile.save()

        # Redirect to a success page or any other desired view
        return redirect('success_page')  # Replace 'success_page' with your desired URL

    # Render the initial form
    return render(request, 'create_profile.html')

def update_profile(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

def employees(request):
    employee = Profile.objects.all().order_by("pk")
    return render(request,"employees.html",{"employee":employee})

def employees2(request):
    user = request.user
    department = user.department
    employee = Profile.objects.filter(department = department)
    return render(request,"employees2.html",{"employee":employee})

def syllabus(request):
    user = request.user
    stream = user.stream
    syllabus = Syl_updates.objects.filter(branch = stream)
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
    user=request.user
    stream = user.department
    subjects= Assign_sub.objects.filter(branch = stream)
    return render(request,"sub_details.html", {"subjects":subjects})

def sub_updates(request):
    username = request.user
    print(username)
    subject=Assign_sub.objects.filter(name= username)
    return render(request,"sub_updates.html", {"subject":subject})

def syl_updates(request):
    if request.method == "POST":
        print("auth")
        # form = forms.Syl_updates(request.POST)
        username = request.user.username
        emp = Profile.objects.filter(username=username).first()
        emp_id=emp.emp_id
        branch=request.POST["branch"]
        subject=request.POST["subject"]
        year=request.POST["year"]
        section=request.POST["section"]
        units=request.POST["units"]
        current=request.POST["current"]
        if emp is not None:
            print(emp.emp_id)
            try:
                temp=Syl_updates.objects.create(subject=subject,branch=branch,year=year,section=section,units=units,current=current,emp_id=emp_id,username=username)   
                return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../emp_home'><button>Goto Home</button></a>")
            except Exception as e:
                return HttpResponse(str(e))
        else:
            return HttpResponse("<p style='color:red; font-size:40px;'>user does not exist</p>")
    print("end")
    return render(request, "syl_updates.html")




# @login_required(login_url = "/login")
def leaves(request):
    if request.method == 'POST':
        name = request.user.username
        email = request.user.email
        stream = request.user.stream
        startdate = request.POST.get('startdate')
        lastdate = request.POST.get('lastdate')
        reason = request.POST.get('reason')
        enterreason = request.POST.get('enterreason')
        try:
            leave = Leaves(name=name, email=email,stream=stream ,startdate=startdate, lastdate=lastdate, reason=reason, enterreason=enterreason)
            leave.save()
            return HttpResponse("<p style='color:green; font-size:40px;'> successfully added </p> <a href='../emp_home'><button>Goto Home</button></a>")
        except Exception as e:
                return HttpResponse(str(e))           
    return render(request, 'leaves.html')


def leaves_report(request):
    user= request.user
    stream = user.stream
    print(stream)
    leaves= Leaves.objects.filter(stream=stream)
    return render(request,"leaves_report.html", {"leaves":leaves},)