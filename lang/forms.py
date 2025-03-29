"""Формы."""

from django import (
    forms,
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.contrib.auth.models import (
    User,
)


class UserLoginForm(AuthenticationForm):
    """Форма авторизации."""

    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50ch'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:50ch'}),
    )


class UserRegisterForm(UserCreationForm):
    """Форма регистрации."""

    username = forms.CharField(
        label='Имя пользователя',
        help_text='Максимум 150 символов',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50ch'}),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:50ch'}),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:50ch'}),
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'width:50ch'}),
    )

    class Meta:
        """Настройки мета-класса."""

        model = User
        fields = ('username', 'email', 'password1', 'password2')
