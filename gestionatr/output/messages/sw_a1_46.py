# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from gestionatr.output.messages.sw_a1_05 import Registerdoclist, Registerdoc


# Paso 01
class MensajeA146(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a1')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A146'}
        )
        self.heading = Heading()
        self.a1 = A146()
        super(MensajeA146, self).__init__('sctdapplication', 'mensaje')


class A146(XmlModel):

    _sort_order = ('a1', 'comreferencenum', 'reqdate', 'reqhour',
                   'operationtype', 'cups', 'extrainfo', 'registerdoclist')

    def __init__(self):
        self.a1 = XmlField('a1')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.operationtype = XmlField('operationtype')
        self.cups = XmlField('cups')
        self.extrainfo = XmlField('extrainfo')
        self.registerdoclist = []
        super(A146, self).__init__('a1', 'a1')

