from django.db import models
from django.urls import reverse
from transliterate import translit, get_available_language_codes, slugify


class Faculty(models.Model):
    """Факультет"""

    title = models.CharField(max_length=50, db_index=True, verbose_name='Название факультета')
    slug = models.SlugField(max_length=50, blank=True, unique=True, verbose_name='Ссылка на факультет')
    info = models.TextField(max_length=500, default=None, verbose_name='Описание факультета')
    image = models.ImageField(default='default.png', blank=True, upload_to='faculty_logos/',
                              verbose_name='Логотип факультета')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('faculty_detail_url', kwargs={'faculty_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Faculty, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Cathedra(models.Model):
    """Кафедра"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Факультет', related_name='cathedras')
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название кафедры')
    slug = models.SlugField(max_length=50, blank=True, unique=True, verbose_name='Ссылка на кафедру')
    info = models.TextField(max_length=500, default=None, verbose_name='Описание кафедры')
    image = models.ImageField(default='default.png', blank=True, upload_to='cathedra_logos/',
                              verbose_name='Логотип кафедры')

    attitude_to_student_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                   verbose_name='Отношение к студентам')
    relevance_of_material_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                     verbose_name='Современность материала')
    availability_of_cathedra_internship_mark = models.DecimalField(blank=True, default=0, max_digits=5,
                                                                   decimal_places=2,
                                                                   verbose_name='Возможность стажировки на кафедре')
    find_job_opportunity_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                    verbose_name='Возможность найти работу')
    teachers_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                        verbose_name='Оценка преподавателей кафедры')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cathedra_detail_url', kwargs={'faculty_slug': self.faculty.slug, 'cathedra_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Cathedra, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class Teacher(models.Model):
    """Преподаватель"""

    cathedras = models.ManyToManyField(Cathedra, related_name='teachers', verbose_name='Кафедры преподавателей')
    first_name = models.CharField(max_length=50, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, db_index=True, verbose_name='Отчество')
    speciality = models.CharField(max_length=50, db_index=True, verbose_name='Специальность')
    avatar = models.ImageField(default='avatar.png', blank=True, upload_to='teachers_avatars/',
                               verbose_name='Фотография преподавателя')
    is_lecturer = models.BooleanField(default=True)
    is_practical = models.BooleanField(default=True)
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    objectivity_lecture_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                   verbose_name='Объективность оценивания (Лектор)')
    objectivity_practice_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                    verbose_name='Объективность оценивания (Практик)')
    knowledge_lecture_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                 verbose_name='Объём знаний по предмету (Лектор)')
    knowledge_practice_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                  verbose_name='Объём знаний по предмету (Практик)')
    communicability_lecture_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                       verbose_name='Связь с аудиторией (Лектор)')
    communicability_practice_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                                        verbose_name='Связь с аудиторией (Практик)')
    teacher_talent_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                              verbose_name='Умение дать материал')
    load_mark = models.DecimalField(blank=True, default=0, max_digits=5, decimal_places=2,
                                    verbose_name='Требовательность')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def get_absolute_url(self):
        return reverse('teacher_detail_url', kwargs={'teacher_id': self.id})

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Course(models.Model):
    """Курс"""

    teachers = models.ManyToManyField(Teacher, related_name='courses', verbose_name='Преподаватели курсов')
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название курса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
