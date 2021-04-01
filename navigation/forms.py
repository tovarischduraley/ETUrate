from django import forms

from .models import *


class FacultyCreationForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'info', 'image',)


class TeacherCreateEditForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple(),
                                             label='Курсы')

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'patronymic', 'courses', 'speciality', 'is_lecturer', 'is_practical',
                  'birth_date', 'avatar')
