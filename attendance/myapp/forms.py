from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=False, label="Username:")
    email = forms.EmailField(required=True, label="Your Email:")
    password = forms.CharField(required=True, label="Password:")