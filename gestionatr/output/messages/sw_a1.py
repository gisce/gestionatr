# -*- coding: utf-8 -*-
from libcomxml.core import XmlModel, XmlField

from gestionatr.output.messages.sw_d1 import Autoconsumo, DatosSuministro, DatosInstGen
from gestionatr.output.messages.base import CabeceraAutoconsumo, CabeceraAutoconsumoRechazo


# Paso 01
class A101(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'info_registro_autocons')

    def __init__(self):
        self.mensaje = XmlField('A101',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = CabeceraAutoconsumo()
        self.info_registro_autocons = InfoRegistroAutoconsA1()
        super(A101, self).__init__('A101', 'mensaje')


class InfoRegistroAutoconsA1(XmlModel):

    _sort_order = ('info_registro_autocons', 'movimiento', 'autoconsumo', 'datos_suministro', 'datos_inst_gen',
                   'comentarios')

    def __init__(self):
        self.info_registro_autocons = XmlField('A101')
        self.movimiento = XmlField('Movimiento')
        self.autoconsumo = Autoconsumo()
        self.datos_suministro = DatosSuministro()
        self.datos_inst_gen = DatosInstGen()
        self.comentarios = XmlField('Comentarios')
        super(InfoRegistroAutoconsA1, self).__init__('InfoRegistoAutoconsA1', 'info_registro_autocons')


# Paso 02
class MensajeA102(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'a102')

    def __init__(self):
        self.mensaje = XmlField('A102',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = CabeceraAutoconsumoRechazo()
        self.a102 = A102()
        super(MensajeA102, self).__init__('A102', 'mensaje')


class A102(XmlModel):

    _sort_order = ('a102', 'cau', 'rechazos', 'comentarios')

    def __init__(self):
        self.a102 = XmlField('A102')
        self.cau = XmlField('CAU')
        self.rechazos = Rechazos()
        self.comentarios = XmlField('Comentarios')
        super(A102, self).__init__('A102', 'a102')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'fecha_rechazo', 'rechazo_list')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.rechazo_list = []
        super(Rechazos, self).__init__('Rechazos', 'rechazos')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'secuencial', 'codigo_motivo', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')
