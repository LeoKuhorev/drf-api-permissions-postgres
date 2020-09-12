from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm, UserUpdateForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ['email', 'username']

    # CREDIT: https://stackoverflow.com/questions/28897480/django-admin-custom-create-user-form
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name',
                  'last_name', 'username', 'password1', 'password2' ),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
