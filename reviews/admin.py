from django.contrib import admin
from .models import LectureReview, PracticeReview, Comment, CathedraReview

admin.site.register(LectureReview)
admin.site.register(PracticeReview)
admin.site.register(Comment)
admin.site.register(CathedraReview)
