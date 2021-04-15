from django.shortcuts import render, get_object_or_404
from .decorators import *
from navigation.models import *
from django.core.mail import send_mail
from RT.settings import EMAIL_HOST_USER
from .forms import *


@staff_only
def admin_panel(request):
    faculties = Faculty.objects.all()
    cathedras = Cathedra.objects.all()
    return render(request, 'admin_panel/admin_panel.html', context={'faculties': faculties, 'cathedras': cathedras})


@staff_only
def faculty_create(request):
    if request.method == 'POST':
        form = FacultyCreateEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel_url')
    else:
        form = FacultyCreateEditForm()
    return render(request, 'admin_panel/faculty_create.html', context={'form': form})


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
    return render(request, 'admin_panel/faculty_edit.html', context={'form': form, 'faculty': faculty})


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
    return render(request, 'admin_panel/cathedra_create.html', context={'form': form})


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
    return render(request, 'admin_panel/cathedra_edit.html', context={'form': form})


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
    return render(request, 'admin_panel/cathedra_head_register.html', context={'form': form})