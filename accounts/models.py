from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Профиль пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    first_name = models.CharField(max_length=50, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, db_index=True, verbose_name='Отчество')
    group_number = models.IntegerField(blank=True, null=True, verbose_name='Номер группы')
    email = models.EmailField(unique=True, max_length=60, verbose_name='email')
    birth_date = models.DateField(default=None, blank=True, verbose_name='Дата рождения')

    is_student = models.BooleanField(default=False)
    is_cathedra_head = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



