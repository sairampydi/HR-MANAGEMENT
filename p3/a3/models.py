from django.db import models
from datetime import datetime
import random

class Leaves(models.Model):
    name = models.CharField(max_length=20)
    # enter_id =  models.AutoField()
    startdate = models.DateField(blank=True, null=True)
    lastdate = models.DateField(blank=True, null=True)
    reason_options = (
        ('vacation', 'Vacation'),
        ('sick-family', 'Sick-Family'),
        ('sick-self', 'Sick-Self'),
        ('funeral', 'Funeral'),
        ('others', 'Others'),
    )
    reason = models.CharField(max_length=100, choices=reason_options, default= "vacation")
    enterreason = models.CharField(max_length=100 ,null = True)

    def __str__(self):
        return self.name
    
class Salary(models.Model):
    username= models.CharField(max_length=20)
    emp_id = models.IntegerField(default= 1)
    amount = models.IntegerField(default= 10000)
    date = models.DateField(default=datetime.now)
    Time= models.TimeField(default=datetime.now)

    def __str__(self):
        return self.username

class Profile(models.Model):
    username= models.CharField(max_length=20)
    email = models.EmailField()
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    emp_id = models.IntegerField(default=123)
    dob = models.DateField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50)
    city= models.CharField(max_length=30)
    country = models.CharField(max_length=30) 
    postal_code = models.IntegerField(default=12345) 

    def __str__(self):
        return self.username 
    
class Assign_sub(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField(default= 1)
    branch = models.CharField(max_length=30)
    year = models.IntegerField(default= 1)
    section = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.name
     