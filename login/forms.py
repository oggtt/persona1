from django import forms

class AuthForm(forms.Form):
    emailA = forms.CharField(label='Your Email Auth')
    passwordA = forms.CharField(label='Password Auth')