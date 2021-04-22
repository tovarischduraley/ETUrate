from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = Profile(
                email=form.cleaned_data['email'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                patronymic=form.cleaned_data['patronymic'],
                group_number=form.cleaned_data['group_number'],
                is_student=True,
                is_active=False
            )
            profile.set_password(form.cleaned_data['password1'])
            profile.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', context={'form': form})


@login_required
def my_profile(request):
    return render(request, 'accounts/my_profile.html', context={'user': request.user})
