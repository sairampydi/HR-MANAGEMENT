from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from accounts.models import User

class Userform(UserCreationForm):
    # date_created = forms.DateField()
    # employee_id = forms.CharField(max_length=32)
    branch = forms.CharField(max_length = 20)
    class Meta :
        model= User
        fields = UserCreationForm.Meta.fields + ('branch',)
        def save(self, commit=True):
            user = super().save(commit=False)
            user.branch = self.cleaned_data['branch']
            if commit:
                user.save()
            return user