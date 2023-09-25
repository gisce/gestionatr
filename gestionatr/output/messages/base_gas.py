# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from libcomxml.core import XmlModel, XmlField


class Heading(XmlModel):
    _sort_order = ('heading', 'dispatchingcode',
                   'dispatchingcompany', 'destinycompany',
                   'communicationsdate', 'communicationshour', 'processcode',
                   'messagetype')

    def __init__(self):
        self.heading = XmlField('heading')
        self.dispatchingcode = XmlField('dispatchingcode')
        self.dispatchingcompany = XmlField('dispatchingcompany')
        self.destinycompany = XmlField('destinycompany')
        self.communicationsdate = XmlField('communicationsdate')
        self.communicationshour = XmlField('communicationshour')
        self.processcode = XmlField('processcode')
        self.messagetype = XmlField('messagetype')
        super(Heading, self).__init__('heading', 'heading')


class Cabecera(XmlModel):
    _sort_order = ('cabecera', 'codenvio',
                   'empresaemisora', 'empresadestino',
                   'fechacomunicacion', 'horacomunicacion', 'codproceso',
                   'tipomensaje')

    def __init__(self):
        self.cabecera = XmlField('cabecera')
        self.codenvio = XmlField('codenvio')
        self.empresaemisora = XmlField('empresaemisora')
        self.empresadestino = XmlField('empresadestino')
        self.fechacomunicacion = XmlField('fechacomunicacion')
        self.horacomunicacion = XmlField('horacomunicacion')
        self.codproceso = XmlField('codproceso')
        self.tipomensaje = XmlField('tipomensaje')
        super(Cabecera, self).__init__('cabecera', 'cabecera')
