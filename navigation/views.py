from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Faculty, Cathedra, Teacher


def index(request):
    return render(request, 'navigation/index.html')


def faculties_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'navigation/faculties_list.html', context={'faculties': faculties})


def faculty_detail(request, faculty_slug):
    faculty = get_object_or_404(Faculty, slug__iexact=faculty_slug)
    return render(request, 'navigation/faculty_detail.html', context={'faculty': faculty})


def cathedra_detail(request, faculty_slug, cathedra_slug):
    cathedra = get_object_or_404(Cathedra, slug__iexact=cathedra_slug)
    return render(request, 'navigation/cathedra_detail.html', context={'cathedra': cathedra})


def teacher_detail(request):
    pass
