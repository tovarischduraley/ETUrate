from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile
from .models import *


class FacultyCreateEditForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'info', 'image',)


class TeacherCreateEditForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), label='Курсы')

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'patronymic', 'courses', 'speciality', 'is_lecturer', 'is_practical',
                  'birth_date', 'avatar',)


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title',)


class CourseEditForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all(), label='Курсы')

    class Meta:
        model = Course
        fields = ('title', 'teachers',)


class CathedraCreateEditForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea, required=True, label='Описание кафедры')

    class Meta:
        model = Cathedra
        fields = ('title', 'info', 'image',)