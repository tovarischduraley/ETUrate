from django import forms
from datetime import date

from accounts.models import Profile
from navigation.models import *


class FacultyCreateEditForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'info', 'image',)


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title',)

    def clean_title(self):
        new_title = self.cleaned_data['title'].capitalize()
        return new_title


class CathedraCreateEditForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea, required=True, label='Описание кафедры')

    class Meta:
        model = Cathedra
        fields = ('title', 'info', 'image',)


class CathedraHeadRegisterForm(forms.ModelForm):
    cathedra = forms.ModelChoiceField(queryset=Cathedra.objects.all(), required=True, label='Кафедра')
    patronymic = forms.CharField(widget=forms.TextInput, label='Отчество', required=False)

    class Meta:
        model = Profile
        fields = ('email', 'last_name', 'first_name', 'patronymic', 'cathedra')
