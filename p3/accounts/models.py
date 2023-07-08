from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import uuid


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
    email = models.EmailField()
    position = models.CharField(max_length=30,default="none",choices= position_options)
    date_created = models.DateField(default=datetime.now)
    joining_letter = models.ImageField(upload_to="account/images",default="None")
    department = models.CharField(max_length=20,default = "none")




