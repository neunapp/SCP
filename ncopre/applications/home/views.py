# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView


class IndexView(TemplateView):
    '''
     clase principal
    '''
    template_name = 'home/index.html'
