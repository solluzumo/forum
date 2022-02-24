from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class RegisterForm(UserCreationForm):

    class Meta:

        model = CustomUser
        fields = ['username', 'email','first_name','last_name','password1',
                  'password2','sex','avatar','specialization','age']



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','avatar','specialization','status']

