from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users, ContactForm
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InputContact(ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"

