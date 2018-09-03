# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from gestionatr.output.messages.sw_a1_05 import Registerdoclist, Registerdoc


# Paso 01
class MensajeA144(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a1')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A144'}
        )
        self.heading = Heading()
        self.a1 = A144()
        super(MensajeA144, self).__init__('sctdapplication', 'mensaje')


class A144(XmlModel):

    _sort_order = ('a1', 'comreferencenum', 'sourcetype', 'firstname',
                   'lastname', 'secondname', 'cups', 'operationtype',
                   'description', 'operationnum', 'prefixtel1', 'telephone1',
                   'prefixtel2', 'telephone2', 'reqdate', 'reqhour', 'readingdate',
                   'readingvalue', 'extrainfo', 'registerdoclist')

    def __init__(self):
        self.a1 = XmlField('a1')
        self.comreferencenum = XmlField('comreferencenum')
        self.sourcetype = XmlField('sourcetype')
        self.firstname = XmlField('firstname')
        self.lastname = XmlField('lastname')
        self.secondname = XmlField('secondname')
        self.cups = XmlField('cups')
        self.operationtype = XmlField('operationtype')
        self.description = XmlField('description')
        self.operationnum = XmlField('operationnum')
        self.prefixtel1 = XmlField('prefixtel1')
        self.telephone1 = XmlField('telephone1')
        self.prefixtel2 = XmlField('prefixtel2')
        self.telephone2 = XmlField('telephone2')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.readingdate = XmlField('readingdate')
        self.readingvalue = XmlField('readingvalue')
        self.extrainfo = XmlField('extrainfo')
        self.registerdoclist = Registerdoclist()
        super(A144, self).__init__('a1', 'a1')

