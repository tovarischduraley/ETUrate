from django import forms

from .models import *

widget = forms.NumberInput(attrs={
    'class': 'review__slider',
    'type': 'range',
    'min': '0',
    'max': '10',
    'step': '1',
    'value': '0',
    'list': 'tickmarks'
})


class TeacherReviewForm(forms.Form):
    objectivity_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Объективность оценивания")
    knowledge_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Знание предмета")
    communicability_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Контакт с аудиторией")

    class Meta:
        fields = ['objectivity_mark', 'knowledge_mark', 'communicability_mark', 'special_mark']


class LectureReviewForm(TeacherReviewForm, forms.Form):
    special_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Подача материала")


class PracticeReviewForm(TeacherReviewForm, forms.Form):
    special_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget, label="Подача материала")


comment_widget = forms.Textarea(attrs={
    'class': 'comment__input',
    'placeholder': 'Оставьте ваш комментарий...'
})


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=comment_widget, max_length=500, required=True)

    class Meta:
        model = Comment
        fields = ['text']


class CathedraReviewForm(forms.ModelForm):
    attitude_to_student_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                  label="Качество образования")
    relevance_of_material_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                    label="Актуальность направлений")
    availability_of_cathedra_internship_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                                  label="Актуальность учебных планов")
    find_job_opportunity_mark = forms.IntegerField(min_value=0, max_value=10, widget=widget,
                                                   label="Возможности для трудоустройств")

    class Meta:
        model = CathedraReview
        fields = ['attitude_to_student_mark', 'relevance_of_material_mark', 'availability_of_cathedra_internship_mark',
                  'find_job_opportunity_mark']
