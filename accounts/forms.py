from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class PasswordInput(forms.PasswordInput):
    input_type = 'password'

class UserForm(UserCreationForm):
    username = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Введите пароль")
    password2 = forms.CharField(label="Подтвердите пароль")

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "patronymic", "group_number", "birth_date"]

