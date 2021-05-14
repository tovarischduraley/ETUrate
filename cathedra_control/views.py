from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from RT.settings import EMAIL_HOST_USER
from .decorators import *
from .forms import *
from .utils import create_report


@cathedra_head_only
def cathedra_control(request):
    search_query = request.GET.get('search', '___123___')
    teachers = request.user.cathedra.teachers.all()
    other_teachers = Teacher.objects.exclude(cathedras__id__contains=request.user.cathedra.id).filter(
        Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) |
        Q(patronymic__icontains=search_query))
    if request.method == 'POST':
        form = ReportDatesForm(request.POST)
        if form.is_valid():
            date_1 = form.cleaned_data['date_1']
            date_2 = form.cleaned_data['date_2']
            if date_1 < date_2:
                file = create_report(request.user.cathedra,
                                     date_1,
                                     date_2 + timedelta(days=1))
                email = EmailMessage('Отчет',
                                     f'Доборого времени суток!\nСформирован отчет по кафедре {request.user.cathedra.title} '
                                     f'за период с {date_1.strftime("%d.%m.%Y")} до {date_2.strftime("%d.%m.%Y")}'
                                     f'\n\nС уважением,\nадминистрация сайта ETUrate',
                                     EMAIL_HOST_USER,
                                     [request.user.email])
                email.attach_file(file)
                email.send(fail_silently=False)
                return redirect('cathedra_control_url')
            else:
                raise forms.ValidationError("Первая дата должна быть меньше второй")
    else:
        form = ReportDatesForm()
    return render(request, 'cathedra_control/cathedra_control.html',
                  context={'teachers': teachers, 'other_teachers': other_teachers, 'form': form})


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
    return render(request, 'cathedra_control/teacher_create.html', context={'form': form})


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
    return render(request, 'cathedra_control/teacher_edit.html', context={'form': form})


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
            form.save()
            return redirect('courses_url')
    else:
        form = CourseCreateForm()
    return render(request, 'cathedra_control/courses.html', context={'form': form, 'courses': courses})


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
    return render(request, 'cathedra_control/course_edit.html', context={'form': form, 'course': course})


# @cathedra_head_only
# def course_delete(request, course_id=None):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == 'POST':
#         course.delete()
#         return redirect('courses_url')


@cathedra_head_only
def add_teacher_to_cathedra(request, teacher_id=None):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        request.user.cathedra.teachers.add(teacher)
        return redirect('cathedra_control_url')


@cathedra_head_only
def add_course_to_teacher(request, teacher_id=None):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    courses = teacher.courses.all()
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            course = Course.objects.filter(title=title).first()
            if course is None:
                course = Course(title=title)
                course.save()
            teacher.courses.add(course)
        return redirect('add_course_to_teacher_url', teacher_id)
    else:
        form = CourseCreateForm()
    return render(request, 'cathedra_control/add_course_to_teacher.html', context={'form': form, 'courses': courses,
                                                                                   'teacher': teacher})
