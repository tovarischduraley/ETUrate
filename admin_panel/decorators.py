from functools import wraps
from django.shortcuts import redirect


def staff_only(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func
