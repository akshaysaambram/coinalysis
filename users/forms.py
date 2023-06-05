from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'mt-3'}))
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    # password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    # password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':'Confirm your Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']