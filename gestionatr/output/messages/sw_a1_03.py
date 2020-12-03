# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading


# Paso 01
class MensajeA103(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a103')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A103'}
        )
        self.heading = Heading()
        self.a103 = A103()
        super(MensajeA103, self).__init__('sctdapplication', 'mensaje')


class A103(XmlModel):

    _sort_order = ('a103', 'comreferencenum', 'comreferencenumanul', 'reqdate', 'reqhour',
                   'titulartype', 'nationality', 'documenttype', 'documentnum',
                   'cups', 'annulmentreason', 'extrainfo')

    def __init__(self):
        self.a103 = XmlField('a103')
        self.comreferencenum = XmlField('comreferencenum')
        self.comreferencenumanul = XmlField('comreferencenumanul')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.titulartype = XmlField('titulartype')
        self.nationality = XmlField('nationality')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.cups = XmlField('cups')
        self.annulmentreason = XmlField('annulmentreason')
        self.extrainfo = XmlField('extrainfo')
        super(A103, self).__init__('a103', 'a103')

