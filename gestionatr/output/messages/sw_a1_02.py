# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading


# Paso 01
class MensajeA102(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a102')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A102'}
        )
        self.heading = Heading()
        self.a102 = A102()
        super(MensajeA102, self).__init__('sctdapplication', 'mensaje')


class A102(XmlModel):

    _sort_order = ('a102', 'comreferencenum', 'reqdate', 'reqhour',
                   'titulartype', 'nationality', 'documenttype',
                   'documentnum', 'cups', 'reqqd', 'reqestimatedqa',
                   'modeffectdate', 'reqtransferdate',
                   'disconnectedserviceaccepted', 'extrainfo')

    def __init__(self):
        self.a102 = XmlField('a102')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.titulartype = XmlField('titulartype')
        self.nationality = XmlField('nationality')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.cups = XmlField('cups')
        self.reqqd = XmlField('reqqd')
        self.reqestimatedqa = XmlField('reqestimatedqa')
        self.modeffectdate = XmlField('modeffectdate')
        self.reqtransferdate = XmlField('reqtransferdate')
        self.disconnectedserviceaccepted = XmlField('disconnectedserviceaccepted')
        self.extrainfo = XmlField('extrainfo')
        super(A102, self).__init__('a102', 'a102')
