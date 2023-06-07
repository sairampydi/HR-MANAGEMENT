from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from accounts.models import User

class Userform(UserCreationForm):
    # date_created = forms.DateField()
    # employee_id = forms.CharField(max_length=32)
    stream = forms.CharField(max_length = 20) 
    position = forms.ChoiceField(choices=(
        ('hod', 'Hod'),
        ('employee', 'Employee'),
        ))
    class Meta :
        model= User
        fields = UserCreationForm.Meta.fields + ('stream','position')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.stream = self.cleaned_data['stream']
        if commit:
            user.save()
        return user