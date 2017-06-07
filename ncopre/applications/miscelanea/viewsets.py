
#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#local import
from .serializers import (
    ObservationListSerializer,
    ObservationStateUpdateSerializer,
    ObservationAddSerializer,
    ServiceAddThirdSerializer
)

from .models import Observation, Service

from applications.proceso.models import Process



class ObservationListViewSet(viewsets.ModelViewSet):
    """viewset para observaciones por proceso"""

    serializer_class = ObservationListSerializer
    def get_queryset(self):
       pk = self.kwargs['pk']
       queryset = Observation.objects.observacion_tipo(pk)
       return queryset



class ObservationStateUpdateViewSet(viewsets.ViewSet):
    """Viewset para actualizar observacion estado de anulado"""

    def create(self, request):
        serializado = ObservationStateUpdateSerializer(data=request.data)
        if serializado.is_valid():
            observation = Observation.objects.get(pk=serializado.validated_data['pk'])
            observation.anulate = serializado.validated_data['anulate']
            observation.save()
            print 'Miscelanea estado actualizado'
        else:
            print serializado.errors

        return Response()



class ObservationAddViewSet(viewsets.ViewSet):
    """ViewSet para agregar obsevacion"""

    def create(self, request):
        serializado = ObservationAddSerializer(data=request.data)
        if serializado.is_valid():

            observation = Observation(
               process=serializado.validated_data['process'],
               description=serializado.validated_data['description'],
               type_observation =serializado.validated_data['type_observation'],
            )
            observation.save()
            print "Miscelanea guardada"
        else:
            print serializado.errors

        return Response()



class ServiceAddThirdViewSet(viewsets.ViewSet):
    """viewset para registar procesos por terceros"""

    def create(self, request):
        serializado = ServiceAddThirdSerializer(data=request.data)

        if serializado.is_valid():
            process = Process.objects.get(pk=serializado.validated_data['process'])
            process.Third=True
            process.save()
            service = Service(
                name=serializado.validated_data['name'],
                ruc=serializado.validated_data['ruc'],
                razon_social=serializado.validated_data['razon_social'],
                phone=serializado.validated_data['phone'],
                description=serializado.validated_data['description'],
                process=process,
            )
            service.save()

            print "Service guardada"
        else:
            print serializado.errors

        return Response()