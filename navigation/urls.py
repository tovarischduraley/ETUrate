from django.conf.urls.static import static
from django.urls import path, include

from RT import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cathedra-control/', include('cathedra_control.urls')),
    path('admin-panel/', include('admin_panel.urls')),
    path('search/', search, name='search_url'),
    path('faculties/', faculties_list, name='faculties_list_url'),
    path('teachers/teacher_id=<int:teacher_id>/', teacher_detail, name='teacher_detail_url'),
    path('<str:faculty_slug>/', faculty_detail, name='faculty_detail_url'),
    path('<str:faculty_slug>/<str:cathedra_slug>/', cathedra_detail, name='cathedra_detail_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
