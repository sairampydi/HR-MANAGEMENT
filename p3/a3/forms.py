from django import forms
from. import models
from accounts.models import User


class Leaves(forms.ModelForm):
    class Meta:
        model = models.Leaves
        fields =( "name","startdate","lastdate","enterreason", "reason", )
    
        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            # emp_id = cleaned_data.get('emp_id')
            try:
                User.objects.get(username=name)
                pass
            except:
                self.add_error('username', 'User does not exists.')
                
            # Check if product with same name and price exists in the database
            # existing_User = User.objects.filter(username=name, emp_id=emp_id).first()
            # if not existing_User:
            #     raise forms.ValidationError('user name and employee id is incorrect')

class Assign_sub(forms.ModelForm):
    class Meta:
        model = models.Assign_sub
        fields =("name","emp_id","branch","year","section","subject",)
        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            # emp_id = cleaned_data.get('emp_id')
            try:
                User.objects.get(username=name)
                pass
            except:
                self.add_error('username', 'User does not exists.')

class Salary(forms.ModelForm):
    class Meta:
        model = models.Salary
        fields =("username","emp_id","amount",)
        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            # emp_id = cleaned_data.get('emp_id')
            try:
                User.objects.get(username=name)
                pass
            except:
                self.add_error('username', 'User does not exists.')

class Profile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields =( "username","email","firstname","lastname","emp_id","dob","mobile","address","city","country","postal_code", )
        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')
            # emp_id = cleaned_data.get('emp_id')
            try:
                User.objects.get(username=name)
                pass
            except:
                self.add_error('username', 'User does not exists.')