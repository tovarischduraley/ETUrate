from django.conf.urls.static import static
from django.urls import path

from RT import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cathedra-control/', cathedra_control, name='cathedra_control_url'),
    path('cathedra-control/teacher-create', teacher_create, name='teacher_create_url'),
    path('admin-panel/', admin_panel, name='admin_panel_url'),
    path('admin-panel/faculty-create/', faculty_create, name='faculty_creation_url'),
    path('faculties/', faculties_list, name='faculties_list_url'),
    path('teachers/teacher_id=<int:teacher_id>/', teacher_detail, name='teacher_detail_url'),
    path('<str:faculty_slug>/', faculty_detail, name='faculty_detail_url'),
    path('<str:faculty_slug>/<str:cathedra_slug>/', cathedra_detail, name='cathedra_detail_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
