"""RT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts import views as accounts_views
from django.contrib.auth import views as auth_views, password_validation

from accounts.forms import UserLoginForm, NewPasswordResetForm, NewSetPasswordForm, NewPasswordChangeForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=UserLoginForm),
         name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name="logout"),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html',
                                                                   form_class=NewPasswordChangeForm),
         name='password_change'),
    path('password-change/done',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',
                                              form_class=NewPasswordResetForm),
         name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                                     form_class=NewSetPasswordForm),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name="password_reset_complete"),
    path('', include('navigation.urls')),
]
