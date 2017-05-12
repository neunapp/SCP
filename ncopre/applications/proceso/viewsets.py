#import django
from django.shortcuts import get_object_or_404

#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#local import
from .serializers import BussinesUnitAddSerializer, BussinesUnitUpdateSerializer, BussinesUnitRetrieveSerializer, ProcessAddSerializer, ListUserSerializer, BussinesUnitUpdateStateAnulateSerializer, ProcessListSerializer
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
    """serializador para recuperar unidad de negocio"""

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



class ProcessAddViewSet(viewsets.ViewSet):
    """viewset paraagregar Proceso"""

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
                date_start = serializado.validated_data['date_start'],
                date_end = serializado.validated_data['date_end'],
                budget_estimated = serializado.validated_data['budget_estimated'],
                budget_real = serializado.validated_data['budget_real'],
                created_by = self.request.user,
                modified_by = self.request.user,
            )

            process.save()
            print 'process guardado'
        else:
            print serializado.errors

        return Response()



class ProcessListForBussinesUnitViewSet(viewsets.ModelViewSet):
    """VIewset para listar process por unidad de negocio"""

    serializer_class = ProcessListSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Process.objects.process_bunit(pk)
        return queryset



class ListUserViewSet(viewsets.ModelViewSet):
    """VIewset usuairo"""

    serializer_class = ListUserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset



class ProcesoUnidadNegocioFilterEnprocesoViewSet(viewsets.ModelViewSet):
    """viewset para listar filtros para proceso por unidad de negocio"""

    serializer_class = ProcessListSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        flat = self.kwargs['flat']
        queryset=Process.objects.proceso_filtro(pk, flat)
        return queryset



