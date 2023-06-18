from django.db import models
from datetime import datetime

class Leaves(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True , null=True)
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
    
class Feedback(models.Model):
    name = models.CharField(max_length=20)
    # enter_id =  models.AutoField()
    CS_options = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('improvement', 'Improvement'),
        ('below', 'Below'),
    )
    CommunicationSkills= models.CharField(max_length=100, choices=CS_options, default= "below")
    TC_options = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('improvement', 'Improvement'),
        ('below', 'Below'),
    )
    TeamworkandCollaboration= models.CharField(max_length=100, choices=TC_options, default= "below")
    PT_options = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('improvement', 'Improvement'),
        ('below', 'Below'),
    )
    ProductivityandTimeManagement= models.CharField(max_length=100, choices=PT_options, default= "below")
    PW_options = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('improvement', 'Improvement'),
        ('below', 'Below'),
    )
    ProfessionalismandWorkEthic= models.CharField(max_length=100, choices=PW_options, default= "below")
    JS_options = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('improvement', 'Improvement'),
        ('below', 'Below'),
    )
    JobKnowledgeandSkills= models.CharField(max_length=100, choices=JS_options, default= "below")
    date = models.DateField(blank=True, null=True)
    comments= models.CharField(max_length=100 ,null = True)
    officername = models.CharField(max_length=20)
    Position= models.CharField(max_length=20)


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
    image = models.ImageField(upload_to="account/images", default="",)
    username= models.CharField(max_length=20)
    surname= models.CharField(max_length=20)
    email = models.EmailField()
    emp_id = models.IntegerField(default=123)
    dob = models.DateField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50)
    city= models.CharField(max_length=30)
    country = models.CharField(max_length=30) 
    state= models.CharField(max_length=30 , default="btech") 
    education = models.CharField(max_length=30,default="btech") 
    experience = models.CharField(max_length=30,default="none" ) 
    details = models.CharField(max_length=30, default="none") 
    postal_code = models.IntegerField(default=12345) 
   

    def __str__(self):
        return self.username 
    
class Assign_sub(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField(default= 1)
    branch = models.CharField(max_length=30)
    year = models.IntegerField(default= 1)
    section = models.IntegerField(default=0)
    subject = models.CharField(max_length=30)
    date = models.DateTimeField( default= datetime.now)

    def __str__(self):
        return self.name
     

class Syl_updates(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField(default= 1)
    subject = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    startdate = models.DateField(blank=True, null=True)
    units = models.CharField(max_length= 30)
    current = models.CharField(max_length= 30)

    def __str__(self):
        return self.name
     