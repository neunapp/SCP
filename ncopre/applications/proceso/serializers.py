from __future__ import absolute_import

from rest_framework import serializers

# local import
from .models import BussinesUnit, Process

# import from other app
from applications.users.models import User


class BussinesUnitAddSerializer(serializers.ModelSerializer):
    """Serializador para agregar Unidad de negocio"""

    class Meta:
        model = BussinesUnit
        fields = (
            'ruc',
            'razon_social',
            'addresses',
            'phone'
        )



class BussinesUnitRetrieveSerializer(serializers.ModelSerializer):
    """Serializador para recuperar  Unidad de negocio"""

    class Meta:
        model = BussinesUnit
        fields = (
            'pk',
            'ruc',
            'razon_social',
            'addresses',
            'phone'
        )



class BussinesUnitUpdateSerializer(serializers.ModelSerializer):
     """Serializador para  actualizar Unidad de negocio"""

     pk = serializers.CharField()
     class Meta:
        model = BussinesUnit
        fields = (
             'pk',
             'ruc',
             'razon_social',
             'addresses',
             'phone'
         )


class BussinesUnitUpdateStateAnulateSerializer(serializers.ModelSerializer):
    """Serializador para actualizar estado de unidad de negocio"""

    pk = serializers.CharField()
    anulate = serializers.BooleanField()

    class Meta:
        model = BussinesUnit
        fields = (
            'pk',
            'anulate'
        )


class ProcessAddSerializer(serializers.ModelSerializer):
    """Seriazlizador para agregar proceso"""

    bussinesunit = serializers.CharField()
    attendant = serializers.CharField()
    responsible = serializers.CharField()
    class Meta:
        model = Process
        fields = (
            'bussinesunit',
            'name',
            'attendant',
            'responsible',
            'date_start',
            'date_end',
            'budget_estimated',
            'budget_real'
        )


class ProcessListSerializer(serializers.ModelSerializer):
    """Serializador para listar Process"""

    class Meta:
        model = Process
        fields = (
            'bussinesunit',
            'name',
            'attendant',
            'responsible',
            'created',
            'date_created',
            'date_started',
            'finished',
            'close',
            'budget_estimated',
            'budget_real'
        )


class ProcessGetSerializer(serializers.ModelSerializer):
    """serializ para recuperar un proceso"""

    class Meta:
        model = Process
        fields = '__all__'


class ProcessNowListSerializer(serializers.ModelSerializer):
    """Serializador para listar Process con su pk"""

    class Meta:
        model = Process
        fields = (
            'pk',
            'bussinesunit',
            'name',
            'attendant',
            'responsible',
            'created',
            'date_created',
            'date_started',
            'finished',
            'close',
            'budget_estimated',
            'budget_real'
        )

class ProcessNameListSerializer(serializers.ModelSerializer):
    """Serializador para listar Process con su nombre """
    name = serializers.CharField()
    class Meta:
        model = Process
        fields = (
            'pk',
            'bussinesunit',
            'name',
            'attendant',
            'responsible',
            'created',
            'date_created',
            'date_started',
            'finished',
            'close',
            'budget_estimated',
            'budget_real'
        )
