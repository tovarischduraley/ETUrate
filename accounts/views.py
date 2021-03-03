from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect

from .forms import UserForm, ProfileForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # user = User(username=user_form.cleaned_data['username'],
            #             password=user_form.cleaned_data['password1'])
            # profile = Profile(first_name=profile_form.cleaned_data['first_name'],
            #                   last_name=profile_form.cleaned_data['last_name'],
            #                   patronymic=profile_form.cleaned_data['patronymic'],
            #                   group_number=profile_form.cleaned_data['group_number'],
            #                   birth_date=profile_form.cleaned_data['birth_date'],
            #                   user=user
            #                   )
            # user.save()
            # profile.save()
            return redirect('home')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'accounts/register.html', context={
        'user_form': user_form,
        'profile_form': profile_form,
    })
