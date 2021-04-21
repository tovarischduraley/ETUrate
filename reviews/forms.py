from django import forms
from datetime import date

from django.forms import NumberInput

from .models import *


class TeacherReviewForm(forms.Form):
    objectivity_mark = forms.IntegerField(min_value=0, max_value=10,
                                          widget=NumberInput(attrs={'type': 'range', 'step': '1'}))
    knowledge_mark = forms.IntegerField(min_value=0, max_value=10,
                                        widget=NumberInput(attrs={'type': 'range', 'step': '1'}))
    communicability_mark = forms.IntegerField(min_value=0, max_value=10,
                                              widget=NumberInput(attrs={'type': 'range', 'step': '1'}))
    special_mark = forms.IntegerField(min_value=0, max_value=10,
                                      widget=NumberInput(attrs={'type': 'range', 'step': '1'}))
    choice = forms.BooleanField(required=False)

    class Meta:
        fields = ['objectivity_mark', 'knowledge_mark', 'communicability_mark', 'special_mark', 'choice']

