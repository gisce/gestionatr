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
class MensajeActualizacionRegistroAutoconsumo(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'actualizacion_registro_autoconsumo')

    def __init__(self):
        self.mensaje = XmlField('A102',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = CabeceraAutoconsumoRechazo()
        self.actualizacion_registro_autoconsumo = ActualizacionRegistroAutoconsumo()
        super(MensajeActualizacionRegistroAutoconsumo, self).__init__('MensajeActualizacionRegistroAutoconsumo', 'mensaje')


class ActualizacionRegistroAutoconsumo(XmlModel):

    _sort_order = ('actualizacion_registro_autoconsumo', 'cau', 'actualizacion_datos_registro',
                   'rechazos', 'comentarios')

    def __init__(self):
        self.actualizacion_registro_autoconsumo = XmlField('A102')
        self.cau = XmlField('CAU')
        self.actualizacion_datos_registro = ActualizacionDatosRegistro()
        self.rechazos = Rechazos()
        self.comentarios = XmlField('Comentarios')
        super(ActualizacionRegistroAutoconsumo, self).__init__('A102', 'actualizacion_registro_autoconsumo')


class ActualizacionDatosRegistro(XmlModel):

    _sort_order = ('actualizacion_datos_registro', 'sub_seccion')

    def __init__(self):
        self.actualizacion_datos_registro = XmlField('ActualizacionDatosRegistro')
        self.sub_seccion = XmlField('SubSeccion')
        super(ActualizacionDatosRegistro, self).__init__('ActualizacionDatosRegistro', 'actualizacion_datos_registro')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'rechazo_list')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.rechazo_list = []
        super(Rechazos, self).__init__('Rechazos', 'rechazos')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'fecha_rechazo', 'secuencial', 'codigo_motivo', 'cups', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.cups = XmlField('CUPS')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')
