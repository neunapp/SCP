# -*- encoding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate


from django import forms
from .models import User



class LoginForm(forms.Form):
    """
        Form para iniciar sesion
    """
    username = forms.CharField(
        label = 'Nombre de Usuario',
        max_length = '35',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Nombre de Usuario',
                'autofocus': 'autofocus',
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'password',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        print authenticate(username=username)

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('nombre de usuario ó password incorrectos.')
        else:
            return self.cleaned_data
