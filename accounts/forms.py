from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField, SetPasswordForm
from transliterate.utils import _

from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm

widget = forms.TextInput(attrs={
    'class': 'input__text',
})

group_widget = forms.TextInput(attrs={
    'class': 'input__text',
    'id': 'group_number',
})

password_input = forms.PasswordInput(attrs={
    'class': 'input__text',
})


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input__text', 'placeholder': ''}), label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input__text',
            'placeholder': '',
        }
    ), label='Пароль')


class NewPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'input__text'}))


class NewSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input__text'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="Подтвердите новый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input__text'}),
    )


class NewPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Старый пароль",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input__text'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password1 = forms.CharField(
        label="Новый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input__text'}),
    )
    new_password2 = forms.CharField(
        label="Подтвердите новый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input__text'}),
    )


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=widget, required=True, label='Имя')
    last_name = forms.CharField(widget=widget, required=True, label='Фамилия')
    patronymic = forms.CharField(widget=widget, required=False, label='Отчество')
    group_number = forms.IntegerField(widget=group_widget, min_value=0, max_value=9999, required=True,
                                      label='Номер группы')
    email = forms.EmailField(widget=widget, label='Email')
    password1 = forms.CharField(widget=password_input, label='Пароль')
    password2 = forms.CharField(widget=password_input, label='Подтвердите пароль')

    class Meta:
        model = Profile
        fields = ["last_name", "first_name", "patronymic", "group_number", "email", "password1", "password2"]


class ProfileCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ("email", "last_name", "first_name", "patronymic", "group_number")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(ProfileCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = (
            'email', 'password', 'last_name', 'first_name', 'patronymic', 'group_number', 'is_staff', 'is_active',
            'is_student', 'is_cathedra_head')

    def clean_password(self):
        return self.initial["password"]
