from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Link

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вставьте ссылку',
            })
        }