from django import forms
from .models import *


class FacultyCreationForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'info', 'image',)


class TeacherCreationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'patronymic', 'speciality', 'is_lecturer', 'is_practical', 'birth_date',
                  'avatar')
