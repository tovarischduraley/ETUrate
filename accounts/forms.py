from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "patronymic", "email", "password1", "password2"]
