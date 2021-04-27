from celery import shared_task
from django.db.models import Avg

from navigation.models import Teacher, Cathedra
from reviews.models import LectureReview, PracticeReview, CathedraReview


@shared_task
def update_teachers_marks():
    teachers = Teacher.objects.all()
    for teacher in teachers:
        if LectureReview.objects.filter(teacher_id=teacher.id).aggregate(Avg('objectivity_mark'))[
            'objectivity_mark__avg'] == None:
            teacher.objectivity_lecture_mark = 0
            teacher.knowledge_lecture_mark = 0
            teacher.communicability_lecture_mark = 0
            teacher.teacher_talent_mark = 0
        else:
            teacher.objectivity_lecture_mark = LectureReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('objectivity_mark'))['objectivity_mark__avg']
            teacher.knowledge_lecture_mark = LectureReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('knowledge_mark'))['knowledge_mark__avg']
            teacher.communicability_lecture_mark = LectureReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('communicability_mark'))['communicability_mark__avg']
            teacher.teacher_talent_mark = LectureReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('teacher_talent_mark'))['teacher_talent_mark__avg']

        if PracticeReview.objects.filter(teacher_id=teacher.id).aggregate(Avg('objectivity_mark'))[
            'objectivity_mark__avg'] == None:
            teacher.objectivity_practice_mark = 0
            teacher.knowledge_practice_mark = 0
            teacher.communicability_practice_mark = 0
            teacher.load_mark = 0
        else:
            teacher.objectivity_practice_mark = PracticeReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('objectivity_mark'))['objectivity_mark__avg']
            teacher.knowledge_practice_mark = PracticeReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('knowledge_mark'))['knowledge_mark__avg']
            teacher.communicability_practice_mark = PracticeReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('communicability_mark'))['communicability_mark__avg']
            teacher.load_mark = PracticeReview.objects.filter(teacher_id=teacher.id).aggregate(
                Avg('load_mark'))['load_mark__avg']
        teacher.save()


@shared_task
def update_cathedras_marks():
    cathdras = Cathedra.objects.all()
    for cathedra in cathdras:
        if CathedraReview.objects.filter(cathedra_id=cathedra.id).aggregate(Avg('attitude_to_student_mark'))[
            'attitude_to_student_mark__avg'] == None:
            cathedra.attitude_to_student_mark = 0
            cathedra.relevance_of_material_mark = 0
            cathedra.availability_of_cathedra_internship_mark = 0
            cathedra.find_job_opportunity_mark = 0
        else:
            cathedra.attitude_to_student_mark = \
                CathedraReview.objects.filter(cathedra_id=cathedra.id).aggregate(Avg('attitude_to_student_mark'))[
                    'attitude_to_student_mark__avg']
            cathedra.relevance_of_material_mark = \
                CathedraReview.objects.filter(cathedra_id=cathedra.id).aggregate(Avg('relevance_of_material_mark'))[
                    'relevance_of_material_mark__avg']
            cathedra.availability_of_cathedra_internship_mark = \
                CathedraReview.objects.filter(cathedra_id=cathedra.id).aggregate(
                    Avg('availability_of_cathedra_internship_mark'))['availability_of_cathedra_internship_mark__avg']
            cathedra.find_job_opportunity_mark = \
                CathedraReview.objects.filter(cathedra_id=cathedra.id).aggregate(Avg('find_job_opportunity_mark'))[
                    'find_job_opportunity_mark__avg']

        teachers = cathedra.teachers.all()

        lecture_sum = 0
        count_of_lecture_reviews = 0
        for teacher in teachers:
            if len(LectureReview.objects.filter(teacher_id=teacher.id)):
                for review in LectureReview.objects.filter(teacher_id=teacher.id):
                    lecture_sum += review.objectivity_mark + review.knowledge_mark + review.communicability_mark + review.teacher_talent_mark
                    count_of_lecture_reviews += 1
        lecture_sum /= 4

        practice_sum = 0
        count_of_practice_reviews = 0
        for teacher in teachers:
            if len(PracticeReview.objects.filter(teacher_id=teacher.id)):
                for review in PracticeReview.objects.filter(teacher_id=teacher.id):
                    practice_sum += review.objectivity_mark + review.knowledge_mark + review.communicability_mark + review.load_mark
                    count_of_practice_reviews += 1
        practice_sum /= 4

        result_count = count_of_practice_reviews + count_of_lecture_reviews
        if result_count:
            cathedra.teachers_mark = (lecture_sum + practice_sum) / result_count
        else:
            cathedra.teachers_mark = 0

        cathedra.save()
