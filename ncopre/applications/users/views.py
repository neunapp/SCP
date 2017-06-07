from django.shortcuts import render

from django.views.generic import (
    CreateView,
    FormView,
    TemplateView
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Autentificacion de usuario
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


class LogInView(FormView):
    '''
        Logeo del usuario
    '''
    template_name = 'users/login.html'
    success_url = reverse_lazy('proceso_app:proceso-index')
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LogInView, self).form_valid(form)
