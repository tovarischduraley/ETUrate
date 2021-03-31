from io import StringIO

from PIL import Image
from django.shortcuts import render, get_object_or_404, redirect

from RT.settings import MEDIA_ROOT
from .forms import FacultyCreationForm, TeacherCreationForm
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


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    cathedras = teacher.cathedras.all()
    return render(request, 'navigation/teacher_detail.html', context={'teacher': teacher, 'cathedras': cathedras})


def cathedra_control(request):
    if request.user.is_cathedra_head:
        teachers = request.user.cathedra.teachers.all()
        return render(request, 'navigation/cathedra_control.html', context={'teachers': teachers})


def teacher_create(request):
    if request.user.is_cathedra_head:
        if request.method == 'POST':
            teacher = Teacher.objects.create()
            teacher.cathedras.add(request.user.cathedra)
            form = TeacherCreationForm(request.POST, instance=teacher)
            if form.is_valid():
                form.save()
                return redirect('cathedra_control_url')
        else:
            form = TeacherCreationForm()
        return render(request, 'navigation/teacher_creation.html', context={'form': form})


"""Дождаться решения по поводу админской панели"""


def admin_panel(request):
    if request.user.is_staff:
        return render(request, 'navigation/admin_panel.html')


def faculty_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = FacultyCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin_panel_url')
        else:
            form = FacultyCreationForm()
        return render(request, 'navigation/faculty_creation.html', context={'form': form})
