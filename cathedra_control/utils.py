from django.db.models import Avg

from navigation.models import Teacher
from reviews.models import LectureReview, PracticeReview

import pandas as pd


def create_report(cathedra, date_1, date_2):
    columns = ['Преподаватель',
               'Объективность оценивания (лекции)',
               'Объём знаний по предмету (лекции)',
               'Связь с аудиторией (лекции)',
               'Умение дать материал (лекции)',
               'Объективность оценивания (практика)',
               'Объём знаний по предмету (практика)',
               'Связь с аудиторией (практика)',
               'Требовательность (практика)']
    teachers = Teacher.objects.filter(cathedras__title__contains=cathedra.title) \
        .order_by('last_name')
    df = pd.DataFrame()
    for teacher in teachers:
        teacher_lecture_marks = LectureReview.objects.filter(teacher=teacher, date__gte=date_1, date__lte=date_2) \
            .aggregate(objectivity_mark=Avg('objectivity_mark'),
                       knowledge_mark=Avg('knowledge_mark'),
                       communicability_mark=Avg('communicability_mark'),
                       teacher_talent_mark=Avg('teacher_talent_mark'))
        if None in teacher_lecture_marks.values():
            teacher_lecture_marks['objectivity_mark'] = '-'
            teacher_lecture_marks['knowledge_mark'] = '-'
            teacher_lecture_marks['communicability_mark'] = '-'
            teacher_lecture_marks['teacher_talent_mark'] = '-'
        teacher_practice_marks = PracticeReview.objects.filter(teacher=teacher, date__gte=date_1, date__lte=date_2) \
            .aggregate(objectivity_mark=Avg('objectivity_mark'),
                       knowledge_mark=Avg('knowledge_mark'),
                       communicability_mark=Avg('communicability_mark'),
                       load_mark=Avg('load_mark'))
        if None in teacher_practice_marks.values():
            teacher_practice_marks['objectivity_mark'] = '-'
            teacher_practice_marks['knowledge_mark'] = '-'
            teacher_practice_marks['communicability_mark'] = '-'
            teacher_practice_marks['load_mark'] = '-'

        data = [f'{teacher.last_name} {teacher.first_name[0]}. {teacher.patronymic[0]}.']
        data += list(teacher_lecture_marks.values())
        data += list(teacher_practice_marks.values())
        df = df.append([data], ignore_index=True)
    df.set_axis(columns, axis='columns', inplace=True)
    df.to_excel('./report.xlsx')
