from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import ProfileManager
from navigation.models import Cathedra


class Profile(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    group_number = models.IntegerField(blank=True, null=True, verbose_name='Номер группы')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email')
    is_staff = models.BooleanField(default=False, verbose_name='Админ')
    is_active = models.BooleanField(default=True, verbose_name='Активный пользователь')
    is_student = models.BooleanField(default=False, verbose_name='Студент')
    is_cathedra_head = models.BooleanField(default=False, verbose_name='Руководитель кафедры')
    username = models.CharField(max_length=30, blank=True)

    cathedra = models.ForeignKey(Cathedra, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                 verbose_name='Кафедра', related_name='cathedra_heads')

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.is_staff or self.is_superuser:
            return self.email
        elif self.patronymic is None:
            return self.last_name + ' ' + self.first_name
        else:
            return self.last_name + ' ' + self.first_name + ' ' + self.patronymic

    def get_initials(self):
        if self.is_staff or self.is_superuser:
            return self.email
        elif self.patronymic is None:
            return self.last_name + ' ' + self.first_name[0] + '.'
        else:
            return self.last_name + ' ' + self.first_name[0] + '. ' + self.patronymic[0] + '.'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
