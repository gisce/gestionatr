# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from sw_a1_41 import Registerdoc, Registerdoclist
from sw_a1_42 import Product, ProductList



# Paso 01
class MensajeA143(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a143')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A143'}
        )
        self.heading = Heading()
        self.a143 = A143()
        super(MensajeA143, self).__init__('sctdapplication', 'mensaje')


class A143(XmlModel):

    _sort_order = (
        'a143',
        'comreferencenum',
        'reqdate',
        'reqhour',
        'titulartype',
        'nationality',
        'documenttype',
        'documentnum',
        'cups',
        'modeffectdate',
        'reqtransferdate',
        'productlist',
        'extrainfo',
        'registerdoclist',
    )

    def __init__(self):
        self.a143 = XmlField('a143')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.titulartype = XmlField('titulartype')
        self.nationality = XmlField('nationality')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.cups = XmlField('cups')
        self.modeffectdate = XmlField('modeffectdate')
        self.reqtransferdate = XmlField('reqtransferdate')
        self.productlist = ProductList()
        self.extrainfo = XmlField('extrainfo')
        self.registerdoclist = Registerdoclist()

        super(A143, self).__init__('a143', 'a143')