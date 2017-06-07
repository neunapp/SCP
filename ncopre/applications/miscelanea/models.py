from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

#import model application proceso
from applications.proceso.models import Process

# django import
from django.db import models

#import managers

from managers import MiscelaneaManager

class Service(TimeStampedModel):
    """ Tabla para servicio """
    name = models.CharField(
        'Nombre de Servicio',
        blank=True,
        max_length=100,
    )
    ruc = models.CharField(
        'RUC',
        blank=True,
        max_length=11,
    )
    razon_social = models.CharField(
        'Razon Social',
        blank=True,
        max_length=100,
    )
    phone = models.CharField(
        'Telefono',
        blank=True,
        max_length=100,
    )
    description = models.CharField(
        'Descripcion',
        blank=True,
        max_length=300
    )
    process = models.ForeignKey(Process)


    def __str__(self):
        return self.name


class Observation(TimeStampedModel):
    """ Tabla Observaciones """

    process = models.ForeignKey(
        Process,
    )
    description = models.CharField(
        'Descripcion',
        blank=True,
        max_length=100,
    )
    TYPE_OBSER = (
        ('0', 'Alta'),
        ('1', 'Media'),
        ('2', 'Baja'),
    )
    type_observation = models.CharField(
        'tipo observacion',
        choices=TYPE_OBSER,
        blank=True,
        max_length=2,
    )
    anulate = models.BooleanField(
        default=False,
    )
    objects = MiscelaneaManager()
    def __str__(self):
        return self.description


class Invoice(TimeStampedModel):
    """ Modelo Factura"""

    process = models.ForeignKey(
        Process,
    )
    number = models.CharField(
        'Numero',
        blank=True,
        max_length=100,
    )
    mount = models.DecimalField(
        'Monto',
        blank=True,
        null=True,
        max_digits=7,
        decimal_places=2
    )
    description = models.CharField(
        'Descripcion',
        blank=True,
        max_length=100,
    )

    def __str__(self):
        return self.number
