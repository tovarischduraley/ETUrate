from django import forms
from datetime import date

from accounts.models import Profile
from .models import *


class FacultyCreateEditForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'info', 'image',)


class DateInput(forms.DateInput):
    input_type = 'date'


class TeacherCreateEditForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), label='Курсы')
    birth_date = forms.DateField(widget=DateInput, label='Дата рождения', required=False)

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'patronymic', 'courses', 'speciality', 'is_lecturer', 'is_practical',
                  'birth_date', 'avatar',)

    def clean_birth_date(self):
        new_date = self.cleaned_data.get("birth_date")

        if new_date and new_date > date.today():
            raise forms.ValidationError("Введена недопустимая дата")
        return new_date


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title',)


class CourseEditForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('title', 'teachers',)

    def __init__(self, user, *args, **kwargs):
        super(CourseEditForm, self).__init__(*args, **kwargs)
        self.fields['teachers'].queryset = Teacher.objects.filter(cathedras__title__contains=user.cathedra.title)


class CathedraCreateEditForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea, required=True, label='Описание кафедры')

    class Meta:
        model = Cathedra
        fields = ('title', 'info', 'image',)


class CathedraHeadRegisterForm(forms.ModelForm):
    cathedra = forms.ModelChoiceField(queryset=Cathedra.objects.all(), required=True, label='Кафедра')

    class Meta:
        model = Profile
        fields = ('email', 'last_name', 'first_name', 'patronymic', 'cathedra')