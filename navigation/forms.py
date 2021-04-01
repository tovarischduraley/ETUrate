from django import forms

from .models import *


class FacultyCreateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'info', 'image',)


class TeacherCreateEditForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), label='Курсы')

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'patronymic', 'courses', 'speciality', 'is_lecturer', 'is_practical',
                  'birth_date', 'avatar',)


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title',)


class CourseEditForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all(), label='Курсы')

    class Meta:
        model = Course
        fields = ('title', 'teachers',)