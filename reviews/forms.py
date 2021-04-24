from django import forms
from datetime import date

from django.forms import NumberInput

from .models import *

widget = forms.NumberInput(attrs={
    'class': 'review__slider',
    'type': 'range',
    'min': '0',
    'max': '10',
    'step': '1',
    'value': '0',
})


class TeacherReviewForm(forms.Form):
    objectivity_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Объективность оценивания")
    knowledge_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Объем знаний по предмету")
    communicability_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Связь с аудиторией")

    class Meta:
        fields = ['objectivity_mark', 'knowledge_mark', 'communicability_mark', 'special_mark']
        widgets = {
            'objectivity_mark': {'class': 'form-group'}
        }


class LectureReviewForm(TeacherReviewForm, forms.Form):
    special_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Талант преподавания")


class PracticeReviewForm(TeacherReviewForm, forms.Form):
    special_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Требовательность")


class CathedraReviewForm(forms.ModelForm):
    attitude_to_student_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                  label="Отношение к студентам")
    relevance_of_material_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                    label="Актуальность преподаваемого материала")
    availability_of_cathedra_internship_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                                  label="Возможность стажировки на кафедре")
    find_job_opportunity_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                   label="Возможность найти работу")

    class Meta:
        model = CathedraReview
        fields = ['attitude_to_student_mark', 'relevance_of_material_mark', 'availability_of_cathedra_internship_mark',
                  'find_job_opportunity_mark']
