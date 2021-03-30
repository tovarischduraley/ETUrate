from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile


class ProfileAdmin(UserAdmin):
    # The forms to add and change user instances
    form = ProfileChangeForm
    add_form = ProfileCreationForm

    list_display = ('email', 'last_name', 'first_name', 'patronymic', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональные данные', {'fields': ('last_name', 'first_name', 'patronymic', )}),
        ('Права доступа', {'fields': ('is_staff', 'is_student', 'is_cathedra_head', 'cathedra')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'password1', 'password2', 'last_name', 'first_name', 'patronymic', 'group_number', 'is_staff',
            'is_student', 'is_cathedra_head', 'cathedra')}
         ),
    )


admin.site.register(Profile, ProfileAdmin)
