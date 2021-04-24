from django.shortcuts import get_object_or_404, redirect
from navigation.models import Teacher


class ReviewCreateMixin:
    model = None
    form_model = None

    def post(self, request, teacher_id):
        form = self.form_model(request.POST, request.FILES)
        if form.is_valid():
            teacher = get_object_or_404(Teacher, id=teacher_id)
            self.model.objects.create(
                request.user,
                teacher,
                form.cleaned_data['objectivity_mark'],
                form.cleaned_data['knowledge_mark'],
                form.cleaned_data['communicability_mark'],
                form.cleaned_data['special_mark'],
            )
        return redirect(request.META['HTTP_REFERER'])
