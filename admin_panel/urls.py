from django.conf.urls.static import static
from django.urls import path

from RT import settings
from .views import *

urlpatterns = [
    path('', admin_panel, name='admin_panel_url'),
    path('faculty-create/', faculty_create, name='faculty_create_url'),
    path('faculty-edit/<str:faculty_slug>/', faculty_edit, name='faculty_edit_url'),
    path('faculty-delete/<str:faculty_slug>/', faculty_delete, name='faculty_delete_url'),
    path('<str:faculty_slug>/cathedra-create/', cathedra_create, name='cathedra_create_url'),
    path('cathedra-edit/<str:cathedra_slug>/', cathedra_edit, name='cathedra_edit_url'),
    path('cathedra-delete/<str:cathedra_slug>/', cathedra_delete, name='cathedra_delete_url'),
    path('cathedra-head-register/', cathedra_head_register, name='cathedra_head_register_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
