from django.contrib.auth.models import User
from django.db import models

# Create your models here.

MARK_CHOICES = (
    ('Ужасно', 1),
    ('Плохо', 2),
    ('Нормально', 3),
    ('Хорошо', 4),
    ('Отлично', 5),
)


class TeacherReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objectivity_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Объективность оценивания')
    knowledge_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Объём знаний по предмету')
    communicability_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Связь с аудиторией')
    load_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Требовательность')

    comment = models.TextField(max_length=400, blank=True, verbose_name='Коментарий')
    post_date = models.DateField(auto_now_add=True, verbose_name='Дата отзыва')
