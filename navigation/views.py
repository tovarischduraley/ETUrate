from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *
from .decorators import *


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


@cathedra_head_only
def cathedra_control(request):
    teachers = request.user.cathedra.teachers.all()
    return render(request, 'navigation/cathedra_control.html', context={'teachers': teachers})


@cathedra_head_only
def teacher_create(request):
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


@cathedra_head_only
def teacher_edit(request, teacher_id=None):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        form = TeacherCreateEditForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            teacher.courses.through.objects.filter(teacher_id=teacher_id).delete()
            for course in form.cleaned_data['courses'].all():
                teacher.courses.add(course)
                form.save()
            return redirect('cathedra_control_url')
    else:
        form = TeacherCreateEditForm(instance=teacher, initial={'courses': teacher.courses.all()})
    return render(request, 'navigation/teacher_edit.html', context={'form': form})


@cathedra_head_only
def teacher_delete(request, teacher_id=None):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('cathedra_control_url')


@cathedra_head_only
def course_create(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses_url')
    else:
        form = CourseCreateForm()
    return render(request, 'navigation/courses.html', context={'form': form, 'courses': courses})


@cathedra_head_only
def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseEditForm(request.POST, instance=course)
        if form.is_valid():
            course.teachers.through.objects.filter(course_id=course_id).delete()
            for teacher in form.cleaned_data['teachers'].all():
                course.teachers.add(teacher)
            form.save()
            return redirect('courses_url')
    else:
        form = CourseEditForm(instance=course, initial={'teachers': course.teachers.all()})
    return render(request, 'navigation/course_edit.html', context={'form': form, 'course': course})


@cathedra_head_only
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses_url')


"""Дождаться решения по поводу админской панели"""


@staff_only
def admin_panel(request):
    return render(request, 'navigation/admin_panel.html')


@staff_only
def faculty_create(request):
    if request.method == 'POST':
        form = FacultyCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel_url')
    else:
        form = FacultyCreateForm()
    return render(request, 'navigation/faculty_creation.html', context={'form': form})
