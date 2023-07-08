from django import forms
from. import models
from accounts.models import User
from a3.models import Profile
from django.contrib import messages


# class Leaves(forms.ModelForm):
#     class Meta:
#         model = models.Leaves
#         fields =( "name","email","startdate","lastdate","enterreason", "reason", )
    
#     def save(self):
#         name = self.cleaned_data.get('name')
#         emp_id = self.cleaned_data.get('emp_id')
#         startdate = self.cleaned_data.get('startdate')
#         lastdate = self.cleaned_data.get('lastdate')
#         User.objects.get(username=name,emp_id=emp_id)
#         user = super().save()



class Feedback(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields =( "name","CommunicationSkills","TeamworkandCollaboration","JobKnowledgeandSkills", "ProductivityandTimeManagement" , "ProfessionalismandWorkEthic", "comments" , "officername","Position", "date" )
    
    def save(self):
        name = self.cleaned_data.get('name')
        user = User.objects.filter(username=name).first()
        if not user:
            raise Exception('user not found')
        print(user.date_created, self.request.user.date_created)
        if user.date_created < self.request.user.date_created:
            raise Exception('you cannot give feedback to seniors')
        super().save()
         

# class Assign_sub(forms.ModelForm):
#     class Meta:
#         model = models.Assign_sub
#         fields =("name","branch","year","section","subject")
#     def save(self):
#         name = self.cleaned_data.get('name')
#         branch = self.cleaned_data.get("branch") 
#         year = self.cleaned_data.get("year") 
#         branchs = ["MCA", "EEE", "ECE", "CIVIL", "MECH" ,"CSE","CSD" ,"CSM", "IT" ]
#         bb= branch.upper()
#         if bb not in branchs:
#             messages.success("please select correct branch")
 
#         if year > 4 :
#             messages.success("please enter ")  
#         User.objects.get(username=name)
#         user = super().save()


# class Profile(forms.ModelForm):
#     class Meta:
#         model = models.Profile
#         fields =( "image","username","surname","email","emp_id","dob","mobile","address","city","state","country","postal_code","education","experience","details", "research")
#     def save(self):
#         name = self.cleaned_data.get('name')
#         email = self.cleaned_data.get('name')
#         # User.objects.get(username=name)
#         user = super().save()
#         return user
        


# class Syl_updates(forms.ModelForm):
#     class Meta:
#         model = models.Syl_updates
#         fields = ("subject","branch","section","startdate","units","current")
#     def save(self):
#         branch = self.cleaned_data.get('branch')
#         branchs = ['MCA','CSE','MECH','CIVIL','CSD','CSM','IT','EEE','ECE']

#         bb = branch.upper()
#         if bb not in branchs:
#             raise Exception('branch not found')
#         super().save()