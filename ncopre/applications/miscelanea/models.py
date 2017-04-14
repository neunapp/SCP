from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django import
from django.db import models


class BussinesUnit(TimeStampedModel):
    """ Modelo Unidad de Negocio """
    ruc = models.CharField(
        'Ruc',
        blank=True,
        max_length=11
    )
    razon_social = models.CharField(
        'razon social',
        blank=True,
        max_length=100
    )
    addresses = models.CharField(
        'Direccion',
        blank=True,
        max_length=100,
    )
    phone = models.CharField(
        'Telefono',
        blank=True,
        max_length=100,
    )

    def __str__(self):
        return self.ruc


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
        'Proceso',
        Process
    )
    description = models.CharField(
        'Descripcion',
        blank=True,
        max_length=100,
    )

    def __str__(self):
        return self.description


class Invoice(TimeStampedModel):
    """ Modelo Factura"""

    process = models.ForeignKey(
        'Proceso',
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
