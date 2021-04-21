from django.shortcuts import render, redirect
from .decorators import student_only
from .forms import TeacherReviewForm


@student_only
def create_review(request):
    print(request.POST)
    return redirect(request.META['HTTP_REFERER'])
