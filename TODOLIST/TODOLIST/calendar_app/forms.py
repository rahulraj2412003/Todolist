from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Task

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use the CustomUser model here
        fields = ['username', 'email', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
