from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile

from navigation.models import Teacher, Cathedra


# Create your models here.

class LectureReview(models.Model):
    """Оценка преподавателя как лектора"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='lecture_reviews',
                                verbose_name='Студент')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    objectivity_mark = models.IntegerField(default=0, verbose_name='Объективность оценивания')
    knowledge_mark = models.IntegerField(default=0, verbose_name='Объём знаний по предмету')
    communicability_mark = models.IntegerField(default=0, verbose_name='Связь с аудиторией')
    teacher_talent_mark = models.IntegerField(default=0, verbose_name='Умение дать материал')

    class Meta:
        verbose_name = 'Оценка преподавателя лектора'
        verbose_name_plural = 'Оценки преподавателей лекторов'

    def __str__(self):
        return f'FROM {self.profile.email} TO {self.teacher.last_name} {self.teacher.first_name} {self.teacher.patronymic}'


class PracticeReview(models.Model):
    """Оценка преподавателя как практика"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='practice_reviews',
                                verbose_name='Студент')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    objectivity_mark = models.IntegerField(default=0, verbose_name='Объективность оценивания')
    knowledge_mark = models.IntegerField(default=0, verbose_name='Объём знаний по предмету')
    communicability_mark = models.IntegerField(default=0, verbose_name='Связь с аудиторией')
    load_mark = models.IntegerField(default=0, verbose_name='Требовательность')

    class Meta:
        verbose_name = 'Оценка преподавателя практики'
        verbose_name_plural = 'Оценки преподавателей практики'

    def __str__(self):
        return f'FROM {self.profile.email} TO {self.teacher.last_name} {self.teacher.first_name} {self.teacher.patronymic}'


class Comment(models.Model):
    """Комментарий преподавателю"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Студент')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    student_group_number = models.IntegerField(blank=True, null=True, verbose_name='Номер группы студента')
    text = models.TextField(max_length=300, verbose_name='Текст комментария')
    post_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки комментария')

    def save(self, *args, **kwargs):
        if not self.student_group_number:
            self.student_group_number = self.profile.group_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'FROM {self.profile.email} TO {self.teacher.last_name} {self.teacher.first_name} {self.teacher.patronymic}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class CathedraReview(models.Model):
    """Оценка кафедры"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cathedra_reviews',
                                verbose_name='Студент')
    cathedra = models.ForeignKey(Cathedra, on_delete=models.CASCADE, verbose_name='Кафедра')
    attitude_to_student_mark = models.IntegerField(default=0, verbose_name='Отношение к студентам')
    relevance_of_material_mark = models.IntegerField(default=0, verbose_name='Современность материала')
    availability_of_cathedra_internship_mark = models.IntegerField(default=0,
                                                                   verbose_name='Возможность стажировки на кафедре')
    find_job_opportunity_mark = models.IntegerField(default=0, verbose_name='Возможность найти работу')

    def __str__(self):
        return f'FROM {self.profile.email} TO {self.cathedra.title}'

    class Meta:
        verbose_name = 'Оценка кафедры'
        verbose_name_plural = 'Оценки кафедры'
