from django.db import models


class Faculty(models.Model):
    """Факультет"""

    title = models.CharField(max_length=50, db_index=True, verbose_name='Название факультета')
    slug = models.SlugField(max_length=50, verbose_name='Ссылка на факультет')

    def __str__(self):
        return self.title


class Cathedra(models.Model):
    """Кафедра"""

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Факультет')
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название кафедры')
    slug = models.SlugField(max_length=50, verbose_name='Ссылка на кафедру')
    attitude_to_student_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                   verbose_name='Отношение к студентам')
    relevance_of_material_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                     verbose_name='Современность материала')
    availability_of_cathedra_internship_mark = models.DecimalField(blank=True, null=True, max_digits=5,
                                                                   decimal_places=2,
                                                                   verbose_name='Возможность стажировки на кафедре')
    find_job_opportunity_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                    verbose_name='Возможность найти работу')
    teachers_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                        verbose_name='Оценка преподавателей кафедры')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    """Преподаватель"""

    cathedra = models.ManyToManyField(Cathedra, related_name='teachers', verbose_name='Кафедры преподавателей')
    firstName = models.CharField(max_length=50, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, db_index=True, verbose_name='Отчество')
    speciality = models.CharField(max_length=50, db_index=True, verbose_name='Специальность')
    # TO DO: Image
    is_lecturer = models.BooleanField(default=True)
    is_practical = models.BooleanField(default=True)
    birth_date = models.DateField(default=None, blank=True, verbose_name='Дата рождения')
    objectivity_lecture_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                   verbose_name='Объективность оценивания (Лектор)')
    objectivity_practice_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                    verbose_name='Объективность оценивания (Практик)')
    knowledge_lecture_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                 verbose_name='Объём знаний по предмету (Лектор)')
    knowledge_practice_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                  verbose_name='Объём знаний по предмету (Практик)')
    communicability_lecture_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                       verbose_name='Связь с аудиторией (Лектор)')
    communicability_practice_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                                        verbose_name='Связь с аудиторией (Практик)')
    communicability_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                               verbose_name='Связь с аудиторией (Лектор)')
    teacher_talent_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                              verbose_name='Умение дать материал')
    load_mark = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,
                                    verbose_name='Требовательность')

    def __str__(self):
        return f'{self.firstName} {self.last_name} {self.patronymic}'


class Course(models.Model):
    """Курс"""

    teachers = models.ManyToManyField(Teacher, related_name='courses', verbose_name='Преподаватели курсов')
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название курса')
    slug = models.SlugField(max_length=50, verbose_name='Ссылка на курс')

    def __str__(self):
        return self.title
