from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):

    user_type=forms.ChoiceField(
                    widget=forms.RadioSelect,
                    label="Select your position",
                    choices=(('super-admin','super-admin '),('sttuf','sttuf'),('customer','customer')),
                    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class UserActiveForm(forms.Form):
    code = forms.CharField(max_length=8)
    