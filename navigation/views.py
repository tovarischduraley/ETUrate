from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *
from .decorators import *

from django.db.models import Q


def index(request):
    return render(request, 'navigation/index.html')


def search(request):
    search_query = request.GET.get('search', '')

    if search_query:
        teachers = Teacher.objects.filter(
            Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) |
            Q(patronymic__icontains=search_query))
        cathedras = Cathedra.objects.filter(title__icontains=search_query)
        faculties = Faculty.objects.filter(title__icontains=search_query)
        context = {
            'teachers': teachers,
            'cathedras': cathedras,
            'faculties': faculties
        }
        return render(request, 'navigation/search.html', context=context)
    else:
        return redirect(request.META['HTTP_REFERER'])

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
    return render(request, 'navigation/teacher_create.html', context={'form': form})


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
def course_edit(request, course_id=None):
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
def course_delete(request, course_id=None):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses_url')


@staff_only
def admin_panel(request):
    faculties = Faculty.objects.all()
    cathedras = Cathedra.objects.all()
    return render(request, 'navigation/admin_panel.html', context={'faculties': faculties, 'cathedras': cathedras})


@staff_only
def faculty_create(request):
    if request.method == 'POST':
        form = FacultyCreateEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel_url')
    else:
        form = FacultyCreateEditForm()
    return render(request, 'navigation/faculty_create.html', context={'form': form})


@staff_only
def faculty_edit(request, faculty_slug=None):
    faculty = get_object_or_404(Faculty, slug=faculty_slug)
    if request.method == 'POST':
        form = FacultyCreateEditForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            flag = 0
            alph = list(string.ascii_letters)
            alph.append(" ")
            for l in form.cleaned_data['title']:
                if l not in alph:
                    flag = 1
                    break
            if flag == 0:
                faculty.slug = slugify(form.cleaned_data['title'])
            else:
                faculty.slug = t_slugify(form.cleaned_data['title'])
            form.save()
            return redirect('admin_panel_url')
    else:
        form = FacultyCreateEditForm(instance=faculty)
    return render(request, 'navigation/faculty_edit.html', context={'form': form, 'faculty': faculty})


@staff_only
def faculty_delete(request, faculty_slug=None):
    faculty = get_object_or_404(Faculty, slug=faculty_slug)
    if request.method == 'POST':
        faculty.delete()
        return redirect('admin_panel_url')


@staff_only
def cathedra_create(request, faculty_slug=None):
    faculty = get_object_or_404(Faculty, slug=faculty_slug)
    if request.method == 'POST':
        cathedra = Cathedra.objects.create(faculty=faculty)
        form = CathedraCreateEditForm(request.POST, request.FILES, instance=cathedra)
        if form.is_valid():
            form.save()
            return redirect('admin_panel_url')
    else:
        form = CathedraCreateEditForm()
    return render(request, 'navigation/cathedra_create.html', context={'form': form})


@staff_only
def cathedra_edit(request, cathedra_slug=None):
    cathedra = get_object_or_404(Cathedra, slug=cathedra_slug)
    if request.method == "POST":
        form = CathedraCreateEditForm(request.POST, request.FILES, instance=cathedra)
        if form.is_valid():
            flag = 0
            alph = list(string.ascii_letters)
            alph.append(" ")
            for l in form.cleaned_data['title']:
                if l not in alph:
                    flag = 1
                    break
            if flag == 0:
                cathedra.slug = slugify(form.cleaned_data['title'])
            else:
                cathedra.slug = t_slugify(form.cleaned_data['title'])
            form.save()
            return redirect('admin_panel_url')
    else:
        form = CathedraCreateEditForm(instance=cathedra)
    return render(request, 'navigation/cathedra_edit.html', context={'form': form})


@staff_only
def cathedra_delete(request,  cathedra_slug=None):
    cathedra = get_object_or_404(Cathedra, slug=cathedra_slug)
    if request.method == "POST":
        cathedra.delete()
        return redirect('admin_panel_url')