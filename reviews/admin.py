from django.contrib import admin
from .models import LectureReview, PracticeReview, Comment


admin.site.register(LectureReview)
admin.site.register(PracticeReview)
admin.site.register(Comment)
