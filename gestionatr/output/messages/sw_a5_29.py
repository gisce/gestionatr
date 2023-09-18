# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading


class MensajeA529(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'a529')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A529'}
        )
        self.heading = Heading()
        self.a529 = A529()
        super(MensajeA529, self).__init__('sctdapplication', 'mensaje')


class A529(XmlModel):
    _sort_order = (
        'a529', 'fechacreacion', 'horacreacion', 'cups', 'historicoconsumo', 'validacioncliente', 'tipodocumento', 'numdocumento'
    )

    def __init__(self):
        self.a529 = XmlField('a529')
        self.fechacreacion = XmlField('fechacreacion')
        self.horacreacion = XmlField('horacreacion')
        self.cups = XmlField('cups')
        self.historicoconsumo = XmlField('historicoconsumo')
        self.validacioncliente = XmlField('validacioncliente')
        self.tipodocumento = XmlField('tipodocumento')
        self.numdocumento = XmlField('numdocumento')

        super(A529, self).__init__('a529', 'a529')
