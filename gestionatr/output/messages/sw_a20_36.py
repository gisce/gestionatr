# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading


# Paso 01
class MensajeA2036(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a20')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A2036'}
        )
        self.heading = Heading()
        self.a20 = A20()
        super(MensajeA2036, self).__init__('sctdapplication', 'mensaje')


class A20(XmlModel):

    _sort_order = (
        'a20', 'reqdate', 'reqhour', 'cups', 'province', 'city', 'zipcode', 'streettype', 'street',
        'streetnumber', 'portal', 'staircase', 'floor', 'door'
    )

    def __init__(self):
        self.a20 = XmlField('a20')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.cups = XmlField('cups')
        self.province = XmlField('province')
        self.city = XmlField('city')
        self.zipcode = XmlField('zipcode')
        self.streettype = XmlField('streettype')
        self.street = XmlField('street')
        self.streetnumber = XmlField('streetnumber')
        self.portal = XmlField('portal')
        self.staircase = XmlField('staircase')
        self.floor = XmlField('floor')
        self.door = XmlField('door')

        super(A20, self).__init__('a20', 'a20')
