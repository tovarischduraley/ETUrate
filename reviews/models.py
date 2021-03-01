from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile
# from navigation.models import Teacher

# Create your models here.

MARK_CHOICES = (
    (1, 'Ужасно'),
    (2, 'Плохо'),
    (3, 'Нормально'),
    (4, 'Хорошо'),
    (5, 'Отлично'),
)


class LectureReview(models.Model):
    """Оценка преподавателя как лектора"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Студент')
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    objectivity_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Объективность оценивания')
    knowledge_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Объём знаний по предмету')
    communicability_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Связь с аудиторией')
    teacher_talent_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Умение дать материал')


class PracticeReview(models.Model):
    """Оценка преподавателя как практика"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Студент')
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    objectivity_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Объективность оценивания')
    knowledge_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Объём знаний по предмету')
    communicability_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Связь с аудиторией')
    load_mark = models.IntegerField(choices=MARK_CHOICES, verbose_name='Требовательность')


class Comment(models.Model):
    """Комментарий преподавателю"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Студент')
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    student_group_number = models.IntegerField(blank=True, null=True, verbose_name='Номер группы студента')
    text = models.TextField(max_length=300, verbose_name='Текст комментария')
    post_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки комментария')


    def save(self, *args, **kwargs):
        if not self.student_group_number:
            self.student_group_number = self.profile.group_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Comment by {self.profile.user.username}'
