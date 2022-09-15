from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)