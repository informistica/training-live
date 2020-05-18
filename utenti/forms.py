from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile,ProfileStatus

class FormRegistrazione(UserCreationForm):
    #email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        #fields = "__all__"


class UserChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['city', 'bio','avatar']
        #fields = "__all__"

