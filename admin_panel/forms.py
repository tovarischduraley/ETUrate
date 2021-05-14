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

    def clean_title(self):
        faculties = Faculty.objects.all()
        slugs = []
        for faculty in faculties:
            slugs.append(faculty.slug)
        if self.instance.title == self.cleaned_data['title'] or self.instance.slug == add_slug(self.cleaned_data['title']):
            return self.cleaned_data['title']
        if add_slug(self.cleaned_data['title']) in slugs:
            raise forms.ValidationError("Факультет с таким названием существует")
        return self.cleaned_data['title']


class CathedraCreateEditForm(forms.ModelForm):
    title = forms.CharField(widget=widget, required=True, label='Название кафедры')
    info = forms.CharField(widget=ta_widget, required=True, label='Описание кафедры')

    class Meta:
        model = Cathedra
        fields = ('title', 'info', 'image',)

    def clean_title(self):
        cathedras = Cathedra.objects.all()
        slugs = []
        for cathedra in cathedras:
            slugs.append(cathedra.slug)
        if self.instance.title == self.cleaned_data['title'] or self.instance.slug == add_slug(self.cleaned_data['title']):
            return self.cleaned_data['title']
        if add_slug(self.cleaned_data['title']) in slugs:
            raise forms.ValidationError("Кафедра с таким названием существует")
        return self.cleaned_data['title']



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
