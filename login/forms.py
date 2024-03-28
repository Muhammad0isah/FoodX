from django import forms
from django.forms import EmailInput, NumberInput, PasswordInput, TextInput, fields, widgets
from .models import UserDetails


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserDetails

        fields = [
            'full_name',
            'username',
            'phone_number',
            'email',
            'password',
            'confirm_password'
        ]
        widgets = {
            'full_name': TextInput(attrs={'class': 'container', 'placeholder': 'name'}),
            'username': TextInput(attrs={'class': 'container', 'placeholder': 'username'}),
            'phone_number': TextInput(attrs={'class': 'container', 'placeholder': 'phone'}),
            'email': TextInput(attrs={'class': 'container', 'placeholder': 'email'}),
            'password': PasswordInput(attrs={'class': 'container', 'placeholder': 'password'}),
            'confirm_password': PasswordInput(attrs={'class': 'container', 'placeholder': 'repeat-password'})

        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = [
            'username',
            'password'
        ]
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'password': PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'password', 'id': 'password-field'})
        }
