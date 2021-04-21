from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from reviews.forms import TeacherReviewForm
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

    context = {
        'teacher': teacher,
        'cathedras': cathedras,
    }
    if request.user.is_student:
        if request.method == 'POST':
            return redirect(request.META['HTTP_REFERER'])
        else:
            reviews_of_lecture_teachers = []
            reviews_of_practice_teachers = []
            for lecture_review in request.user.lecture_reviews.all():
                reviews_of_lecture_teachers.append(lecture_review.teacher)
            for practice_review in request.user.practice_reviews.all():
                reviews_of_practice_teachers.append(practice_review.teacher)
            context.update({'reviews_of_lecture_teachers': reviews_of_lecture_teachers,
                            'reviews_of_practice_teachers': reviews_of_practice_teachers})

            lecture_form = TeacherReviewForm(prefix='lform')
            practice_form = TeacherReviewForm(prefix='pform')
            context.update({'lform': lecture_form, 'pform': practice_form})

        return render(request, 'navigation/teacher_detail.html', context=context)
