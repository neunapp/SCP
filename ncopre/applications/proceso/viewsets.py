#import django
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse

#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

#local import
from .serializers import (
    BussinesUnitAddSerializer,
    BussinesUnitUpdateSerializer,
    BussinesUnitRetrieveSerializer,
    ProcessAddSerializer,
    BussinesUnitUpdateStateAnulateSerializer,
    ProcessListSerializer,
    ProcessNameListSerializer,
    ProcessGetSerializer,
    ProcessStateChangeSerializer,
    ProcessByBusinessSerializer,
    ProcessSerializer,

)

from .models import BussinesUnit, Process

# import from other application

from applications.users.models import User


class BussinesUnitAddViewSet(viewsets.ViewSet):
    """viewset para agregar unidad de negocio"""

    def create(self, request):
        serializado = BussinesUnitAddSerializer(data=request.data)
        if serializado.is_valid():
            bussinesunit = BussinesUnit(
                ruc = serializado.validated_data['ruc'],
                razon_social = serializado.validated_data['razon_social'],
                addresses = serializado.validated_data['addresses'],
                phone = serializado.validated_data['phone'],
            )
            bussinesunit.save()
            print 'Unidad de negocio Guardado'
        else:
            print serializado.errors

        return Response()


class BussinesUnitRetriveViewSet(viewsets.ViewSet):
    """viewset para recuperar unidad de negocio"""

    def retrieve(self, request, pk=None):
        unidanegocio = get_object_or_404(BussinesUnit, pk=pk)
        serializer = BussinesUnitRetrieveSerializer(unidanegocio, context={'request': request})
        return Response(serializer.data)


class BussinesUnitUpdateViewSet(viewsets.ViewSet):
    """viewset para actualizar unidad de negocio"""

    def create(self, request):
        serializado = BussinesUnitUpdateSerializer(data=request.data)
        if serializado.is_valid():
            bussines = BussinesUnit.objects.get(pk=serializado.validated_data['pk'])
            bussines.ruc = serializado.validated_data['ruc']
            bussines.razon_social = serializado.validated_data['razon_social']
            bussines.addresses = serializado.validated_data['addresses']
            bussines.phone = serializado.validated_data['phone']
            bussines.anulate = False
            bussines.save()
            print 'Unidad de negocio Actualizado'
        else:
            print serializado.errors

        return Response()



class BussinesUnitUpdateStateAnulateViewSet(viewsets.ViewSet):
    """Viewset para actualizar estado de Unidad de Negocio"""

    def create(self, request):
        serializado = BussinesUnitUpdateStateAnulateSerializer(data=request.data)
        if serializado.is_valid():
            bussines = BussinesUnit.objects.get(pk=serializado.validated_data['pk'])
            bussines.anulate = serializado.validated_data['anulate']
            bussines.save()
            print 'Unidad de negocio estado actualizado Actualizado'
        else:
            print serializado.errors

        return Response()



class BussinesUnitListViewSet(viewsets.ModelViewSet):
    """viewset que lista bussines Unit"""
    serializer_class = BussinesUnitRetrieveSerializer

    def get_queryset(self):
        queryset = BussinesUnit.objects.by_bussines()
        return queryset


class ProcessByBusiness(viewsets.ModelViewSet):
    """Lista proceso agrupados por unidad de negocio"""

    serializer_class = ProcessByBusinessSerializer

    def get_queryset(self):
        queryset = Process.objects.process_by_bussiness()
        return queryset


class ProcessAddViewSet(viewsets.ViewSet):
    """viewset para agregar Proceso"""

    def create(self, request):
        serializado = ProcessAddSerializer(data=request.data)

        if serializado.is_valid():
            bussinesunit = BussinesUnit.objects.get(pk=serializado.validated_data['bussinesunit'])
            attendant = User.objects.get(pk=serializado.validated_data['attendant'])
            responsible = User.objects.get(pk=serializado.validated_data['responsible'])
            process = Process(
                bussinesunit = bussinesunit,
                attendant = attendant,
                responsible = responsible,
                name = serializado.validated_data['name'],
                origin=serializado.validated_data['origin'],
                destination=serializado.validated_data['destination'],
                date_start = serializado.validated_data['date_start'],
                date_end = serializado.validated_data['date_end'],
                budget_estimated = serializado.validated_data['budget_estimated'],
                created_by = self.request.user,
                modified_by = self.request.user,
            )

            process.save()
            print 'process guardado'
            res = {
                'flat':'0',
                'pk':process.pk,
            }
        else:
            res = {
                'flat':'1',
                'pk':'0',
            }
            print serializado.errors

        return Response(res)


class ProcessGetViewSet(viewsets.ViewSet):
    """servicio para recuperar un Proceso por pk"""

    def retrieve(self, request, pk=None):
        proceso = get_object_or_404(Process, pk=pk)
        serializer = ProcessGetSerializer(proceso, context={'request': request})
        return Response(serializer.data)



class ProcessListForBussinesUnitViewSet(viewsets.ModelViewSet):
    """VIewset para listar process por unidad de negocio"""

    serializer_class = ProcessListSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Process.objects.process_bunit(pk)
        return queryset



class ProcesoUnidadNegocioFilterEnprocesoViewSet(viewsets.ModelViewSet):
    """viewset para listar filtros para proceso por unidad de negocio"""

    serializer_class = ProcessListSerializer

    def get_queryset(self):
        pk=self.kwargs['pk']
        flat = self.kwargs['flat']
        queryset=Process.objects.proceso_filtro(pk, flat)
        return queryset



class ProcesoNowUnidadNegocioViewSet(viewsets.ModelViewSet):
    """viewset para listar 50 primeros elementos creados"""

class ProcessRecentViewSet(viewsets.ModelViewSet):
    """lista los 50 procesos mas recientes"""

    serializer_class = ProcessSerializer

    def get_queryset(self):
        queryset =Process.objects.proceso_todos()
        return queryset



class ProcesoSearchViewSet(viewsets.ModelViewSet):
    """viewset para buscar proceso"""

    serializer_class = ProcessSerializer

    def get_queryset(self):
        kwords = self.kwargs['kword']
        queryset = Process.objects.process_search(kwords)
        return queryset



class ProcessStateChangeViewSet(viewsets.ViewSet):
    """viewset para actualizar estados del Proceso"""

    def create(self, request):

        serializado = ProcessStateChangeSerializer(data=request.data)

        if serializado.is_valid():
            pk = Process.objects.get(pk=serializado.validated_data['pk'])
            alternative = serializado.validated_data['alternative']
            if alternative == 'created':
                pk.created = Process.objects.validator_check(pk.created)
                pk.save()
            elif alternative == 'finished':
                pk.finished = Process.objects.validator_check(pk.finished)
                pk.save()
            elif alternative == 'close':
                pk.close = Process.objects.validator_check(pk.close)
                pk.save()
            elif alternative == 'started':
                pk.started = Process.objects.validator_check(pk.started)
                pk.save()
            elif alternative == 'anulate':
                pk.anulate = Process.objects.validator_check(pk.anulate)
                pk.save()
            print 'process guardado'
        else:
            print serializado.errors

        return Response()






