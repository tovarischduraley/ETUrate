from functools import wraps
from django.shortcuts import redirect


def student_only(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_student:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func
