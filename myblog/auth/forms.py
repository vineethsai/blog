from django import forms
from django.forms import CharField, Form, PasswordInput


class RegistrationForm(forms.Form):
    """
    Registration form
    """
    username = forms.CharField(label='Username', max_length=30, required=True)
    password = forms.CharField(label='password', max_length=30, required=True, widget=PasswordInput())
    passwordconf  = forms.CharField(label='passwordconf', max_length=30, required=True, widget=PasswordInput())
    email = forms.CharField(label='email', max_length=30, required=True)
    first_name = forms.CharField(label='first_name', max_length=30, required=True)
    last_name = forms.CharField(label='last_name', max_length=30, required=True)

class SigninForm(forms.Form):
    """
    Signin form
    """
    username = forms.CharField(label='Username', max_length=30, required=True)
    password = forms.CharField(label='password', max_length=30, required=True, widget=PasswordInput())
