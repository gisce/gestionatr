# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from gestionatr.output.messages.sw_a1_41 import Registerdoclist, Registerdoc


# Paso 01
class MensajeA104(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a104')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication',
            attributes={'xmlns': 'http://localhost/sctd/A104'}
        )
        self.heading = Heading()
        self.a104 = A104()
        super(MensajeA104, self).__init__('sctdapplication', 'mensaje')


class A104(XmlModel):

    _sort_order = (
        'a104', 'comreferencenum', 'reqdate', 'reqhour', 'titulartype',
        'nationality', 'documenttype', 'documentnum', 'cups',
        'cancelreason', 'modeffectdate', 'reqcanceldate', 'cancelhour',
        'contactphonenumber', 'extrainfo', 'registerdoclist'
    )

    def __init__(self):
        self.a104 = XmlField('a104')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.titulartype = XmlField('titulartype')
        self.nationality = XmlField('nationality')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.cups = XmlField('cups')
        self.cancelreason = XmlField('cancelreason')
        self.modeffectdate = XmlField('modeffectdate')
        self.reqcanceldate = XmlField('reqcanceldate')
        self.cancelhour = XmlField('cancelhour')
        self.contactphonenumber = XmlField('contactphonenumber')
        self.extrainfo = XmlField('extrainfo')
        self.registerdoclist = Registerdoclist()
        super(A104, self).__init__('a104', 'a104')
