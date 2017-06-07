from django.shortcuts import render

# Create your views here.

from applications.proceso.models import Process

from django.views.generic import (
    CreateView,
    UpdateView,
    TemplateView,
    DetailView,
    FormView,
)

class ProcessDetailMisceleaView(DetailView):
    '''
     clase lista observacion
    '''

    model = Process
    template_name = 'observacion/list_observacion.html'



class ServiceProcessView(DetailView):
    """agregar un nuevo servicio y actualizar proceso"""

    model = Process
    template_name = 'observacion/servicioadd.html'