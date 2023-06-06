from django.contrib import admin
from django.urls import path
from. import views

app_name= "a3"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("leaves",views.leaves,name="leaves"),
    path("leaves_report",views.leaves_report,name="leaves_report"),
    path("nav_bar/",views.nav_bar,name="nav_bar"),
    path("emp_nav/",views.emp_nav,name="emp_nav"),
    path("add_salary/",views.add_salary,name="add_salary"),
    # path("salary_updates/",views.salary_updates,name="salary_updates"),
    path("salary_updates/",views.salary_updates,name="salary_updates"),
    path("sal_details/",views.sal_details,name="sal_details"),
    path("update_employees/",views.update_employees,name="update_employees"),
    path("employees/",views.employees,name="employees"),
    path("hr_home/",views.hr_home,name="hr_home"),
    path("emp_home/",views.emp_home,name="emp_home"),
    path("hr_nav/",views.hr_nav,name="hr_nav"),
    path("profile/",views.profile,name="profile"),
    path("syllabus/",views.syllabus,name="syllabus"),
    path("emp_profile/",views.emp_profile,name="emp_profile"),
    path("feedback/",views.feedback,name="feedback"),
    path("feedbackform/",views.feedbackform,name="feedbackfrom"),
    path("assign_sub/", views.assign_sub , name="assign_sub"),
    path("sub_updates/", views.sub_updates , name="sub_updates"),
    path("syl_updates/", views.syl_updates , name="syl_updates"),
    path("<int:id>/delete/",views.delete_view,name="delete"),
    path("<int:id>/delete_v/",views.delete_v,name="delete_v"),
    path("<int:id>/delete_z/",views.delete_z,name="delete_z"),
    path("<int:id>/accept/",views.accept_view,name="accept"),

    # path("",views.home,name="leaves.html")
]
