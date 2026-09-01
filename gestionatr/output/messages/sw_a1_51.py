# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading


class MensajeA151(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a151')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A151'}
        )
        self.heading = Heading()
        self.a151 = A151()
        super(MensajeA151, self).__init__('sctdapplication', 'mensaje')


class A151(XmlModel):
    _sort_order = ('a151', 'comreferencenum', 'reqdate', 'reqhour', 'cups',
                   'solicitudreferencia', 'tiporeposicion', 'documenttype',
                   'documentnum', 'titulartype', 'extrainfo')

    def __init__(self):
        self.a151 = XmlField('a151')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.cups = XmlField('cups')
        self.solicitudreferencia = XmlField('solicitudreferencia')
        self.tiporeposicion = XmlField('tiporeposicion')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.titulartype = XmlField('titulartype')
        self.extrainfo = XmlField('extrainfo')
        super(A151, self).__init__('a151', 'a151')


class MensajeA2951(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a2951')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A2951'}
        )
        self.heading = Heading()
        self.a2951 = A2951()
        super(MensajeA2951, self).__init__('sctdapplication', 'mensaje')


class A2951(XmlModel):
    _sort_order = ('a2951', 'reqcode', 'reqdate', 'reqhour', 'responsedate',
                   'responsehour', 'cups', 'result', 'resultreason', 'extrainfo')

    def __init__(self):
        self.a2951 = XmlField('a2951')
        self.reqcode = XmlField('reqcode')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.responsedate = XmlField('responsedate')
        self.responsehour = XmlField('responsehour')
        self.cups = XmlField('cups')
        self.result = XmlField('result')
        self.resultreason = XmlField('resultreason')
        self.extrainfo = XmlField('extrainfo')
        super(A2951, self).__init__('a2951', 'a2951')