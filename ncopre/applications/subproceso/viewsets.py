#import django
from django.shortcuts import get_object_or_404

#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#appication proceso
from applications.proceso.models import Process
#aplication item
from applications.item.models import DetailProcess, Item
#impor local
from .serializers import (
    GetProcessActivitySerializer,
    SubProcessSerializer,
    FieldSerializer,
)
#
from .functions import get_activitys_process
#
from .models import (
    SubProcess,
    FieldsSubProcess,
    Field,
)


class GetProcessActivitys(viewsets.ModelViewSet):
    """viewset que lista actividades de un proceso"""
    serializer_class = GetProcessActivitySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = get_activitys_process(pk)
        return queryset


class ActivityProcessAddViewSet(viewsets.ViewSet):
    """viewset para agregar sub proceso a un proceso"""

    def create(self, request):
        print 'Agregando actividad...'
        serializado = SubProcessSerializer(data=request.data)
        if serializado.is_valid():
            print '...'
            #recuperamos proceso y registramos sub proceso
            proceso = Process.objects.get(
                pk=serializado.validated_data['pk_proceso'],
            )
            #
            sub_proceso = SubProcess(
                name=serializado.validated_data['name'],
                description=serializado.validated_data['description'],
            )
            sub_proceso.save()
            print 'sub Proceso guarado'
            #registramos el detalle proceso relacion proceso sub proceso
            detalle_proceso = DetailProcess(
                process=proceso,
                sub_process=sub_proceso,
            )
            detalle_proceso.save()
            print 'detalle proceso guarado'
            #
            print 'Sub Proceso guardado correctamente'
        else:
            print serializado.errors

        return Response()


class FieldAddViewSet(viewsets.ViewSet):
    """viewset para agregar Field o columna a un Subproceso"""

    def create(self, request):
        print 'Agregando field ...'
        serializado = FieldSerializer(data=request.data)
        if serializado.is_valid():
            #agregamos el field
            field = Field(
                name=serializado.validated_data['name'],
                type_field=serializado.validated_data['type_field'],
                required=serializado.validated_data['required'],
            )
            field.save()
            print 'Field guarado'
            #recuperamos sub proceso
            sub_process = SubProcess.objects.get(
                pk=serializado.validated_data['sub_process']
            )
            #registramos la relacion con el proceso
            field_sub_proceso = FieldsSubProcess(
                sub_process=sub_process,
                field=field,
            )
            field_sub_proceso.save()
            print 'Detalle Campos sub proceso guarado'
        else:
            print serializado.errors

        return Response()


class GetSubProcessFields(viewsets.ModelViewSet):
    """viewset que lista Fields de SubProcess"""
    serializer_class = FieldSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = FieldsSubProcess.objects.get_subprocess_fields(pk)
        return queryset
