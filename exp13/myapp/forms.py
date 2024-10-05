from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Enter Username',
            'email': 'Enter Email',
        }

    # Customizing error messages
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'required': 'Username is required.'}
        self.fields['email'].error_messages = {'required': 'Email is required.'}
        self.fields['password1'].error_messages = {
            'required': 'Password is required.',
            'min_length': 'Password must contain at least 8 characters.',
        }
        self.fields['password2'].error_messages = {'required': 'Please confirm your password.'}
