from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django import
from django.conf import settings
from django.db import models

#local model proceso
from applications.proceso.models import Process

#local model sub proceso
from applications.subproceso.models import SubProcess, FieldsSubProcess

#local
from .managers import DetailProcessManager, FieldsVoucherManager


class DetailProcess(TimeStampedModel):
    """ Modelo para Detalle Proeso """

    process = models.ForeignKey(Process)
    sub_process = models.ForeignKey(SubProcess)

    objects = DetailProcessManager()

    def __str__(self):
        return str(self.process)


class Item(TimeStampedModel):
    """ Item description """

    detail_process = models.ForeignKey(
        DetailProcess
    )
    detail_camp_subprocess = models.ForeignKey(
        FieldsSubProcess,
    )
    tipy_item = models.CharField(
        'Tipo',
        blank=True,
        max_length=100,
    )
    value = models.CharField(
        'Valor',
        max_length=300,
    )

    def __str__(self):
        return str(self.detail_process)



class Voucher(TimeStampedModel):
    """ Tabla Voucher """

    TYPE_VOUCHER_CHOICESS = (
        ('0', 'Boleta'),
        ('1', 'Factura'),
        ('2', 'Voucher'),
    )

    type_voucher = models.CharField(
        'Tipo Voucher',
        choices=TYPE_VOUCHER_CHOICESS,
        blank=True,
        max_length=2,
    )
    number = models.CharField(
        'Numero',
        blank=True,
        max_length=20
    )
    amount = models.DecimalField(
        'Monto',
        blank=True,
        null=True,
        max_digits=12,
        decimal_places=3
    )
    description = models.CharField(
        'Descripcion',
        blank=True,
        max_length=300,
    )
    date_broadcast = models.DateField(
        'Fecha Emision',
        blank=True,
        null=True
    )
    anulate = models.BooleanField(
        'anulado',
        default=False
    )
    process = models.ForeignKey(
        Process,
    )
    objects = FieldsVoucherManager()

    def __str__(self):
        return self.number
