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

#local imports
from .models import BussinesUnit



class BussinesUnitAddView(TemplateView):
    """Vista para agregar unidad de negocio"""

    template_name = 'unidadnegocio/add.html'



class BussinesUnitUpdateView(DetailView):
    """Vista para recuperar unidad de negocio"""

    model = BussinesUnit
    template_name = 'unidadnegocio/update.html'



class BussinesUnitLitView(TemplateView):
    '''
     clase lista bussines Unit  2
    '''
    template_name = 'unidadnegocio/list_bussinesUnit.html'



class ProcessAddView(DetailView):
    """Vista para guardar tabla Proceso"""

    model = BussinesUnit
    template_name = 'proceso/add.html'



class ProceessForBunitView(DetailView):
    """vista para mostrar procesos por unidad de negocio"""

    model = BussinesUnit
    template_name = 'proceso/list_processbunit.html'
