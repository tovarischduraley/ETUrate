from django.conf.urls.static import static
from django.urls import path

from RT import settings
from .views import *

urlpatterns = [

    path('', cathedra_control, name='cathedra_control_url'),
    path('courses/', course_create, name='courses_url'),
    path('courses/course-edit/course_id=<int:course_id>/', course_edit, name='course_edit_url'),
    path('courses/course-delete/course_id=<int:course_id>/', course_delete, name='course_delete_url'),
    path('teacher-create/', teacher_create, name='teacher_create_url'),
    path('teacher-edit/teacher_id=<int:teacher_id>/', teacher_edit, name='teacher_edit_url'),
    path('teacher-delete/teacher_id=<int:teacher_id>/', teacher_delete, name='teacher_delete_url'),
    path('add-teacher/teacher_id=<int:teacher_id>/', add_teacher_to_cathedra, name='add_teacher_url'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
