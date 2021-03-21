from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import ProfileManager
from datetime import datetime


class Profile(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=50,  null=True, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, null=True,  blank=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=50,  null=True, blank=True, verbose_name='Отчество')
    group_number = models.IntegerField(blank=True, null=True, verbose_name='Номер группы')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email')
    is_staff = models.BooleanField(default=False, verbose_name='is_staff')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    is_student = models.BooleanField(default=True, verbose_name='is_student')
    is_cathedra_head = models.BooleanField(default=False, verbose_name='is_cathedra_head')
    username = models.CharField(max_length=30, blank=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.is_superuser:
            return 'Superuser'
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'






