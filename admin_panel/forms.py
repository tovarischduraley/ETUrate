from django import forms

from accounts.models import Profile
from navigation.models import *

widget = forms.TextInput(attrs={
    'class': 'input__text',
})

ta_widget = forms.Textarea(attrs={
    'class':'text__area'
})

class FacultyCreateEditForm(forms.ModelForm):
    title = forms.CharField(widget=widget, required=True, label='Название факультета')
    info = forms.CharField(widget=ta_widget, required=True, label='Описание факультета')
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
    title = forms.CharField(widget=widget, required=True, label='Название кафедры')
    info = forms.CharField(widget=ta_widget, required=True, label='Описание кафедры')

    class Meta:
        model = Cathedra
        fields = ('title', 'info', 'image',)


c_widget = forms.Select(attrs={'class': 'select'})


class CathedraHeadRegisterForm(forms.ModelForm):
    cathedra = forms.ModelChoiceField(widget=c_widget, queryset=Cathedra.objects.all(), required=True, label='Кафедра')
    patronymic = forms.CharField(widget=widget, label='Отчество', required=False)
    last_name = forms.CharField(widget=widget, label='Фамилия', required=True)
    first_name = forms.CharField(widget=widget, label='Имя', required=True)
    email = forms.EmailField(widget=widget, label='Email', required=True)

    class Meta:
        model = Profile
        fields = ('email', 'last_name', 'first_name', 'patronymic', 'cathedra')
