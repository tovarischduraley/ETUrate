from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    fields = ['cathedras',
              'first_name',
              'last_name',
              'patronymic',
              'speciality',
              'avatar',
              'is_lecturer',
              'is_practical',
              'birth_date']


class FacultyAdmin(admin.ModelAdmin):
    fields = ['title',
              'info',
              'image']


class CathedraAdmin(admin.ModelAdmin):
    fields = ['faculty',
              'title',
              'info',
              'image']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Cathedra, CathedraAdmin)
admin.site.register(Course)
