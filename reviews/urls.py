from django.urls import path

from .views import *

urlpatterns = [
    path('create/lecture_review/teacher_id<int:teacher_id>', create_lecture_review,
         name='create_lecture_review_url'),
    path('create/practice_review/teacher_id<int:teacher_id>', create_practice_review,
         name='create_practice_review_url'),
    path('create/cathedra_review/cathedra_id<int:cathedra_id>', create_cathedra_review,
         name='create_cathedra_review_url'),
    path('create/comment/teacher_id<int:teacher_id>', create_comment,
         name='create_comment_url'),
    path('delete/comment/comment_id<int:comment_id>/', delete_comment, name='delete_comment_url')

]
