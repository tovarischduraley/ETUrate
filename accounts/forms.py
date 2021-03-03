from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, label='Имя')
    last_name = forms.CharField(required=True, label='Фамилия')
    patronymic = forms.CharField(required=True, label='Отчество')
    group_number = forms.IntegerField(max_value=9999, required=True, label='Номер группы')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "patronymic", "group_number", "email", "password1", "password2"]
