from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2')



class UserUpdateForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'date_of_birth')
