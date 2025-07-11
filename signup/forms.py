from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Your name')
    email = forms.CharField(label='Your Email')
    password = forms.CharField(label='Password')