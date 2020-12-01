# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from sw_a1_41 import Registerdoc, Registerdoclist


# Paso 01
class MensajeA2542(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a2542')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A2542'}
        )
        self.heading = Heading()
        self.a2542 = A2542()
        super(MensajeA2542, self).__init__('sctdapplication', 'mensaje')


class A2542(XmlModel):

    _sort_order = (
        'a2542',
        'reqcode',
        'cups',
        'visitdate',
        'visithour',
        'comreferencenum',
        'informationtype',
        'informationtypedesc',
        'interventiondate',
        'interventionhourfrom',
        'interventionhourto',
        'visitnumber',
        'operationnum',
        'extrainfo',
        'defectlist',
    )

    def __init__(self):
        self.a2542 = XmlField('a2542')
        self.reqcode = XmlField('reqcode')
        self.cups = XmlField('cups')
        self.visitdate = XmlField('visitdate')
        self.visithour = XmlField('visithour')
        self.comreferencenum = XmlField('comreferencenum')
        self.informationtype = XmlField('informationtype')
        self.informationtypedesc = XmlField('informationtypedesc')
        self.interventiondate = XmlField('interventiondate')
        self.interventionhourfrom = XmlField('interventionhourfrom')
        self.interventionhourto = XmlField('interventionhourto')
        self.visitnumber = XmlField('visitnumber')
        self.operationnum = XmlField('operationnum')
        self.extrainfo = XmlField('extrainfo')
        self.defectlist = Defectlist()
        super(A2542, self).__init__('a2542', 'a2542')


class Defectlist(XmlModel):

    _sort_order = ('defectlist', 'defect_list')

    def __init__(self):
        self.defectlist = XmlField('defectlist')
        self.defect_list = []
        super(Defectlist, self).__init__('defectlist', 'defectlist')


class Defect(XmlModel):

    _sort_order = ('defect', 'code', 'description',)

    def __init__(self):
        self.defect = XmlField('defect')
        self.code = XmlField('code')
        self.description = XmlField('description')
        super(Defect, self).__init__('defect', 'defect')
