# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    TemplateView,
    DetailView,
    FormView,
)

#proceso import
from applications.proceso.models import Process



class SubProcessAddView(DetailView):
    """Vista para agregar sub proceso a un proceso"""

    model = Process
    template_name = 'subproceso/add.html'
