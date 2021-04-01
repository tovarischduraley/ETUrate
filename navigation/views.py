from django.shortcuts import render, get_object_or_404, redirect

from .forms import FacultyCreationForm, TeacherCreateEditForm
from .models import *


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
            form = TeacherCreateEditForm(request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                for course in form.cleaned_data['courses'].all():
                    teacher.courses.add(course)
                form.save()
                return redirect('cathedra_control_url')
        else:
            form = TeacherCreateEditForm()
        return render(request, 'navigation/teacher_creation.html', context={'form': form})


def teacher_edit(request, teacher_id=None):
    if request.user.is_cathedra_head:
        teacher = get_object_or_404(Teacher, id=teacher_id)
        if request.method == 'POST':
            form = TeacherCreateEditForm(request.POST, request.FILES, instance=teacher)
            if form.is_valid():
                teacher.courses.through.objects.all().delete()
                for course in form.cleaned_data['courses'].all():
                    teacher.courses.add(course)
                form.save()
                return redirect('cathedra_control_url')
        else:
            form = TeacherCreateEditForm(instance=teacher, initial={'courses': teacher.courses.all()})
        return render(request, 'navigation/teacher_edit.html', context={'form': form})


def teacher_delete(request, teacher_id=None):
    if request.user.is_cathedra_head:
        teacher = get_object_or_404(Teacher, id=teacher_id)
        if request.method == 'POST':
            teacher.delete()
            return redirect('cathedra_control_url')
        else:
            return redirect('cathedra_control_url')


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
