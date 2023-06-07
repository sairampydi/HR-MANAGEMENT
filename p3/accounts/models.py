from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import uuid


# Create your models here.
# class user_signup(models.Models):
class User(AbstractUser):
    employee_options = (
        ('hr', 'HR'),
        ('employee', 'Employee'),
    )
    employee_status = models.CharField(max_length=32,default="employee",choices= employee_options)
    position_options = (
        ('hod', 'Hod'),
        ('employee', 'Employee'),
    )
    position = models.CharField(max_length=30,default="none",choices= position_options)
    employee_id = models.CharField( max_length=5, default=2110, primary_key =True),
    date_created = models.DateField(default=datetime.now)
    branch = models.CharField(max_length=20,default = "none")




