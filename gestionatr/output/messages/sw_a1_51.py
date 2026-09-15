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

class MensajeA2651(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a2651')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A2651'}
        )
        self.heading = Heading()
        self.a2651 = A2651()
        super(MensajeA2651, self).__init__('sctdapplication', 'mensaje')


class A2651(XmlModel):

    _sort_order = ('a2651', 'reqcode', 'cups', 'comreferencenum', 'stateincidence',
                   'contact', 'extrainfo')

    def __init__(self):
        self.a2651 = XmlField('a2651')
        self.reqcode = XmlField('reqcode')
        self.cups = XmlField('cups')
        self.comreferencenum = XmlField('comreferencenum')
        self.stateincidence = XmlField('stateincidence')
        self.contact = contact()
        self.extrainfo = XmlField('extrainfo')
        super(A2651, self).__init__('a2651', 'a2651')

class contact(XmlModel):

    _sort_order = ('contact', 'contactname', 'contacttelephone1', 'contacttelephone2',
                   'contacttelephone3', 'contactemail')

    def __init__(self):
        self.contact = XmlField('contact')
        self.contactname = XmlField('contactname')
        self.contacttelephone1 = XmlField('contacttelephone1')
        self.contacttelephone2 = XmlField('contacttelephone2')
        self.contacttelephone3 = XmlField('contacttelephone3')
        self.contactemail = XmlField('contactemail')
        super(contact, self).__init__('contact', 'contact')