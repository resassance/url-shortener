from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Link

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Имя пользователя"
        self.fields['username'].help_text = ""
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Пароль еще раз"
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Имя пользователя"
        self.fields['password'].label = "Пароль"
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': field.label
            })

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['original_url']
        labels = {'original_url': ''}
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Вставьте длинную ссылку здесь',
            })
        }