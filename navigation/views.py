from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from RT.settings import EMAIL_HOST_USER
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
    other_teachers = Teacher.objects.exclude(cathedras__id__contains=request.user.cathedra.id)
    return render(request, 'navigation/cathedra_control.html',
                  context={'teachers': teachers, 'other_teachers': other_teachers})


@cathedra_head_only
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherCreateEditForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = Teacher.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                patronymic=form.cleaned_data['patronymic'],
                speciality=form.cleaned_data['speciality'],
                is_lecturer=form.cleaned_data['is_lecturer'],
                is_practical=form.cleaned_data['is_practical'],
                birth_date=form.cleaned_data['birth_date'],
                avatar=form.cleaned_data['avatar'],
            )
            teacher.cathedras.add(request.user.cathedra)
            for course in form.cleaned_data['courses'].all():
                teacher.courses.add(course)
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
    cathedra = request.user.cathedra
    if request.method == 'POST':
        cathedra.teachers.remove(teacher)
        return redirect('cathedra_control_url')


@cathedra_head_only
def course_create(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            # course = Course(title=form.cleaned_data['title'].capitalize())
            # course.save()
            form.save()
            return redirect('courses_url')
    else:
        form = CourseCreateForm()
    return render(request, 'navigation/courses.html', context={'form': form, 'courses': courses})


@cathedra_head_only
def course_edit(request, course_id=None):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseEditForm(request.user, request.POST, instance=course)
        if form.is_valid():
            course.teachers.through.objects.filter(course_id=course_id).delete()
            for teacher in form.cleaned_data['teachers'].all():
                course.teachers.add(teacher)
            form.save()
            return redirect('courses_url')
    else:
        form = CourseEditForm(instance=course, user=request.user)
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
        form = CathedraCreateEditForm(request.POST, request.FILES)
        if form.is_valid():
            cathedra = Cathedra.objects.create(
                title=form.cleaned_data['title'],
                info=form.cleaned_data['info'],
                image=form.cleaned_data['image'],
                faculty=faculty
            )
            cathedra.save()
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
            form.save()
            return redirect('admin_panel_url')
    else:
        form = CathedraCreateEditForm(instance=cathedra)
    return render(request, 'navigation/cathedra_edit.html', context={'form': form})


@staff_only
def cathedra_delete(request, cathedra_slug=None):
    cathedra = get_object_or_404(Cathedra, slug=cathedra_slug)
    if request.method == "POST":
        cathedra.delete()
        return redirect('admin_panel_url')


@staff_only
def cathedra_head_register(request):
    if request.method == 'POST':
        form = CathedraHeadRegisterForm(request.POST)
        if form.is_valid():
            profile = Profile(
                email=form.cleaned_data['email'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                patronymic=form.cleaned_data['patronymic'],
                cathedra=form.cleaned_data['cathedra'],
                is_student=False,
                is_cathedra_head=True
            )
            password = Profile.objects.make_random_password()
            profile.set_password(password)
            massage = 'Доброго времени суток, ' + profile.__str__() + '!\n\nВаш пароль: ' + password + \
                      '\n\nС уважением,\nадминистрация сайта ETUrate'
            send_mail('Регистрация руководителя кафедры', massage, EMAIL_HOST_USER,
                      [form.cleaned_data['email']], fail_silently=False)
            profile.save()
            return redirect('admin_panel_url')
    else:
        form = CathedraHeadRegisterForm()
    return render(request, 'navigation/cathedra_head_register.html', context={'form': form})


def add_teacher_to_cathedra(request, teacher_id=None):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        request.user.cathedra.teachers.add(teacher)
        return redirect('cathedra_control_url')
