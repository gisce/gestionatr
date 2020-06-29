# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from gestionatr.output.messages.sw_a1_41 import Registerdoclist, Registerdoc


# Paso 01
class MensajeA149(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a149')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A149'}
        )
        self.heading = Heading()
        self.a149 = A149()
        super(MensajeA149, self).__init__('sctdapplication', 'mensaje')


class A149(XmlModel):

    _sort_order = (
        'a149', 'comreferencenum', 'reqdate', 'reqhour', 'cups', 'comreferencenumdes', 'tipodesistimiento',
        'documenttype', 'documentnum', 'titulartype', 'extrainfo'
    )

    def __init__(self):
        self.a149 = XmlField('a149')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.cups = XmlField('cups')
        self.comreferencenumdes = XmlField('comreferencenumdes')
        self.tipodesistimiento = XmlField('tipodesistimiento')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.titulartype = XmlField('titulartype')
        self.extrainfo = XmlField('extrainfo')

        super(A149, self).__init__('a149', 'a149')

