from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django import
from django.conf import settings
from django.db import models

#local model proceso
from applications.proceso.models import Process

#local model

#local model Subprocess

class DetailProcess(TimeStampedModel):
    """ Modelo para Detalle Proeso """

    process = models.ForeignKey(
        'proceso',
        Process,
    )
    sub_process = models.ForeignKey(SubProcess)

    def __str__(self):
        return str(self.process)


class Item(TimeStampedModel):
    """ Item description """

    detail_process = models.ForeignKey(
        'Detelle Proceso',
        DetailProcess
    )
    detail_camp_subprocess = models.ForeignKey(
        'Detelle Campo Sub Proceso',
        DetailProcess
    )
    tipe_item = models.CharField(
        'Tipo',
        blank=True,
        max_length=100,
    )
    value = models.DecimalField(
        'Valor',
        max_digits=7,
        decimal_places=3,
    )

    def __str__(self):
        return str(detail_process)



class Voucher(TimeStampedModel):
    """ Tabla Voucher """

    tipe_voucher = models.CharField(
        'Tipo Voucher'.
        blank=True,
        max_length=100,
    )
    numner = models.CharField(
        'Numero',
        blank=True,
        max_length=20
    )


    def __str__(self):
        return self.
