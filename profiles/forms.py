from django import forms
from .models import Profile
from django.contrib.auth.models import User


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email")

class FormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ("user",)
