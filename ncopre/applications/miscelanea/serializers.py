
#aplicacion de terceros
from rest_framework import serializers

#libreria local
from models import Observation



class ObservationListSerializer(serializers.ModelSerializer):
    """serializador para listar observaciones"""

    class Meta:

        model = Observation
        fields = (
            'pk',
            'process',
            'description',
            'type_observation',
        )



class ObservationStateUpdateSerializer(serializers.ModelSerializer):
    """serializador que actualiza estado anulado"""
    pk = serializers.CharField()
    anulate = serializers.BooleanField()

    class Meta:

        model = Observation
        fields = (
            'pk',
            'anulate',
        )



class ObservationAddSerializer(serializers.ModelSerializer):
    """Agreagr una observacion"""

    class Meta:

        model = Observation
        fields = (
           'process',
           'description',
           'type_observation',
        )

