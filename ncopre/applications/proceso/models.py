from __future__ import unicode_literals

# django import
from django.conf import settings
from django.db import models

# third-party
from model_utils.models import TimeStampedModel

#import local miscelanea
from applications.miscelanea.models import BussinesUnit, Service


class Process(TimeStampedModel):
    """ Tabla Proceso """

    bussinesunit = models.ForeignKey(
        'Unidad de Negocio',
        BussinesUnit,
    )
    attendant = models.ForeignKey(
        'Encargado',
        settings.AUTH_USER_MODEL,
    )
    responsible = models.ForeignKey(
        'Responsable',
        settings.AUTH_USER_MODEL,
    )
    date_start = models.DateField(
        'Fecha Inicio',
        blank=True,
        null=True
    )
    date_end = models.DateField(
        'Fecha Fin',
        blank=True,
        null=True
    )
    created = models.BooleanField(
        'Creado',
        default=True
    )
    date_created = models.DateField(
        'Fecha Creacion',
        blank=True,
        null=True
    )
    date_started = models.DateField(
        'Fecha Iniciado',
        blank=True,
        null=True
    )
    finished = models.BooleanField(
        'Finalizado',
        default=False,
    )
    date_end = models.DateField(
        'Fecha Fin',
        blank=True,
        null=True
    )
    close = models.BooleanField(
        'Cerrado',
        default=False,
    )
    date_close = models.DateField(
        'Fecha Cerrado',
        blank=True,
        null=True
    )
    started = models.BooleanField(
        'Iniciado',
        default=False
    )
    budget_estimated = models.DecimalField(
        'Presupuesto',
        blank=True,
        null=True,
        max_digits=7,
        decimal_places=2
    )
    budget_real = models.DecimalField(
        'Presupuesto',
        blank=True,
        null=True,
        max_digits=7,
        decimal_places=2
    )
    origin = models.CharField(
        'Origin',
        blank=True,
        max_length=100
    )
    destination = models.CharField(
        'Destino',
        blank=True,
        max_length=100
    )

    def __str__(self):
        return str(self.bussinesunit.name)
