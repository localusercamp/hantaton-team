from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'inn', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
# ------
class CustomUserCreationFormCompanyUniversity(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('inn', 'email')

class CustomUserCreationFormStudentMentor(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'third_name', 'email')

