from django import forms
from datetime import date

from django.forms import NumberInput

from .models import *

widget = forms.NumberInput(attrs={
    'id': 'weightSlider',
    'class': 'tick-slider-input',
    'type': 'range',
    'min': '0',
    'max': '10',
    'step': '1',
    'value': '0',
    'data-tick-step': '5',
    'data-tick-id': 'weightTicks',
    'data-value-id': 'weightValue',
    'data-progress-id': 'weightProgress',
    'data-handle-size': '18',
    'data-min-label-id': 'weightLabelMin',
    'data-max-label-id': 'weightLabelMax',
})


class TeacherReviewForm(forms.Form):
    objectivity_mark = forms.IntegerField(min_value=0, max_value=10,
                                          widget=widget,
                                          label="Объективность оценивания")
    knowledge_mark = forms.IntegerField(min_value=0, max_value=10,
                                        widget=widget,
                                        label="Объем знаний по предмету")
    communicability_mark = forms.IntegerField(min_value=0, max_value=10,
                                              widget=widget,
                                              label="Связь с аудиторией")

    class Meta:
        fields = ['objectivity_mark', 'knowledge_mark', 'communicability_mark', 'special_mark']
        widgets = {
            'objectivity_mark': {'class': 'form-group'}
        }


class LectureReviewForm(TeacherReviewForm):
    special_mark = forms.IntegerField(min_value=0, max_value=10,
                                      widget=widget,
                                      label="Талант преподавания")


class PracticeReviewForm(TeacherReviewForm):
    special_mark = forms.IntegerField(min_value=0, max_value=10,
                                      widget=widget,
                                      label="Требовательность")
