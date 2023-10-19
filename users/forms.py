from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "bio", "profile_photo", "password1", "password2"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'profile_photo']