from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from navigation.models import Teacher, Cathedra
from .decorators import student_only
from .forms import LectureReviewForm, PracticeReviewForm, CathedraReviewForm
from .models import LectureReview, PracticeReview, CathedraReview
from .utils import ReviewCreateMixin


# @student_only
# class CreateLectureReviewView(ReviewCreateMixin, View):
#     model = LectureReview
#     form_model = LectureReviewForm


@student_only
def create_lecture_review(request, teacher_id):
    if request.method == 'POST':
        form = LectureReviewForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = get_object_or_404(Teacher, id=teacher_id)
            LectureReview.objects.create(
                profile=request.user,
                teacher=teacher,
                objectivity_mark=form.cleaned_data['objectivity_mark'],
                knowledge_mark=form.cleaned_data['knowledge_mark'],
                communicability_mark=form.cleaned_data['communicability_mark'],
                teacher_talent_mark=form.cleaned_data['special_mark'],
            )
    return redirect(request.META['HTTP_REFERER'])


@student_only
def create_practice_review(request, teacher_id):
    if request.method == 'POST':
        form = PracticeReviewForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = get_object_or_404(Teacher, id=teacher_id)
            PracticeReview.objects.create(
                profile=request.user,
                teacher=teacher,
                objectivity_mark=form.cleaned_data['objectivity_mark'],
                knowledge_mark=form.cleaned_data['knowledge_mark'],
                communicability_mark=form.cleaned_data['communicability_mark'],
                load_mark=form.cleaned_data['special_mark'],
            )
    return redirect(request.META['HTTP_REFERER'])


@student_only
def create_cathedra_review(request, cathedra_id):
    if request.method == 'POST':
        form = CathedraReviewForm(request.POST, request.FILES)
        if form.is_valid():
            cathedra = get_object_or_404(Cathedra, id=cathedra_id)
            CathedraReview.objects.create(
                profile=request.user,
                cathedra=cathedra,
                attitude_to_student_mark=form.cleaned_data['attitude_to_student_mark'],
                relevance_of_material_mark=form.cleaned_data['relevance_of_material_mark'],
                availability_of_cathedra_internship_mark=form.cleaned_data['availability_of_cathedra_internship_mark'],
                find_job_opportunity_mark=form.cleaned_data['find_job_opportunity_mark'],
            )
    return redirect(request.META['HTTP_REFERER'])
