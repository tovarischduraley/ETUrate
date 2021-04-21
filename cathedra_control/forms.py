from django import forms
from datetime import date
from navigation.models import *


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

    def clean_title(self):
        new_title = self.cleaned_data['title'].capitalize()
        return new_title


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'teachers',)

    def __init__(self, user, *args, **kwargs):
        super(CourseEditForm, self).__init__(*args, **kwargs)
        self.fields['teachers'].queryset = Teacher.objects.filter(cathedras__title__contains=user.cathedra.title)

    def clean_title(self):
        new_title = self.cleaned_data['title'].capitalize()
        return new_title