from django.urls import path
from. import views

app_name ="accounts"

urlpatterns = [
    path("signup/",views.signup_views, name="signup"),
    path("hr_login/",views.hr_login, name="hr_login"),
    path("logout/",views.logout_views, name="logout"),
    path("user_login/",views.user_login, name="user_login"),
    path("hod_login/",views.hod_login, name="hod_login"),
    path("user_signup/",views.user_signup, name="user_signup"),
]