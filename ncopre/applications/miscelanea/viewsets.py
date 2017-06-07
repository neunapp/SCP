
#libraries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response

#local import
from .serializers import (
    ObservationListSerializer,
    ObservationStateUpdateSerializer,
    ObservationAddSerializer
)

from .models import Observation



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
            print 'Observacion estado actualizado'
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
            print "Observacion guardada"
        else:
            print serializado.errors

        return Response()
