from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from accounts.models import User

class Userform(UserCreationForm):
    department = forms.CharField(max_length = 20) 
    joining_letter = forms.ImageField()
    position = forms.ChoiceField(choices=(
        ('hod', 'Hod'),
        ('employee', 'Professor'),
        ))
    email = forms.EmailField()
    class Meta :
        model= User
        fields = UserCreationForm.Meta.fields + ('department','position','email','joining_letter')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.stream = self.cleaned_data['stream']
        if commit:
            user.save()
        return user