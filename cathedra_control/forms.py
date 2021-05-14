from django import forms
from datetime import date

from navigation.models import *

widget = forms.TextInput(attrs={
    'class': 'input__text',
})

s_widget = forms.CheckboxSelectMultiple(attrs={

})
c_widget = forms.TextInput(attrs={'class': 'input__text__short'})


class DateInput(forms.DateInput):
    input_type = 'date'


class TeacherCreateEditForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=s_widget, label='Курсы',
                                             required=False)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата рождения', required=False)
    last_name = forms.CharField(widget=widget, label='Фамилия', required=True)
    first_name = forms.CharField(widget=widget, label='Имя', required=True)
    patronymic = forms.CharField(widget=widget, label='Отчество', required=False)
    speciality = forms.CharField(widget=widget, label='Специальность', required=False)

    class Meta:
        model = Teacher
        fields = ('last_name', 'first_name', 'patronymic', 'courses', 'speciality', 'is_lecturer', 'is_practical',
                  'birth_date', 'avatar',)

    def clean_birth_date(self):
        new_date = self.cleaned_data.get("birth_date")

        if new_date and new_date > date.today():
            raise forms.ValidationError("Введена недопустимая дата")
        return new_date


class CourseCreateForm(forms.ModelForm):
    title = forms.CharField(widget=widget, max_length=50, label='Название курса')

    class Meta:
        model = Course
        fields = ('title',)

    def clean_title(self):
        courses = Course.objects.all()
        titles = []
        for course in courses:
            titles.append(course.title.lower())
        title = self.cleaned_data['title']
        title = title.lower()
        if title in titles:
            raise forms.ValidationError("Курс с таким названием уже существует")
        else:
            return self.cleaned_data['title']


class CourseEditForm(forms.ModelForm):
    title = forms.CharField(widget=widget, max_length=50, label='Название курса')
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all(), widget=s_widget, label='Преподаватели',
                                              required=False)

    class Meta:
        model = Course
        fields = ('title', 'teachers',)

    def __init__(self, user, *args, **kwargs):
        super(CourseEditForm, self).__init__(*args, **kwargs)
        self.fields['teachers'].queryset = Teacher.objects.filter(cathedras__title__contains=user.cathedra.title)

    def clean_title(self):
        courses = Course.objects.all()
        titles = []
        for course in courses:
            titles.append(course.title.lower())
        title = self.cleaned_data['title']
        title = title.lower()
        if title in titles:
            raise forms.ValidationError("Курс с таким названием уже существует")
        else:
            return self.cleaned_data['title']

    def full_clean(self):
        if self.date_1 > self.date_2:
            raise forms.ValidationError("Первая дата должна быть меньше второй")


widget1 = forms.DateInput(attrs={'type': 'date', 'class': 'date__field}'})


class ReportDatesForm(forms.Form):
    date_1 = forms.DateField(widget=widget1, label='С ')
    date_2 = forms.DateField(widget=widget1, label='По ')

    def clean(self):
        cleaned_data = super().clean()

        date1 = cleaned_data.get('date_1')
        if date1 and date1 > date.today():
            raise forms.ValidationError("Введена недопустимая дата1")

        date2 = cleaned_data.get('date_2')
        if date2 and date2 > date.today():
            raise forms.ValidationError("Введена недопустимая дата2")

        if date1 > date2:
            raise forms.ValidationError("Введен некорректный временной отрезок(дата1 > дата2)")
