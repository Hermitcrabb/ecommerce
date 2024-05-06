from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterform(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={"placeholder":"Email"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    
    
    
    class Meta:
        model = User
        fields = [
            'username', 'email','password1',
            ]
        