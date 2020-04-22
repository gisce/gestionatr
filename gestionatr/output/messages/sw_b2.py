# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_b1 import *


# Paso 05
class MensajeActivacionBajaUnidireccional(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_baja')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionBajaUnidireccional',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_baja = ActivacionBaja()
        super(MensajeActivacionBajaUnidireccional, self).__init__('MensajeActivacionBajaUnidireccional', 'mensaje')


class ActivacionBaja(XmlModel):

    _sort_order = ('activacion_baja', 'datos_activacion_baja', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_baja = XmlField('ActivacionBaja')
        self.datos_activacion_baja = DatosActivacionBaja()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionBaja, self).__init__('ActivacionBaja', 'activacion_baja')


class DatosActivacionBaja(XmlModel):

    _sort_order = ('datos_activacion_baja', 'motivo', 'fecha_activacion')

    def __init__(self):
        self.datos_activacion_baja = XmlField('DatosActivacionBaja')
        self.motivo = XmlField('Motivo')
        self.fecha_activacion = XmlField('FechaActivacion')
        super(DatosActivacionBaja, self).__init__('DatosActivacionBaja', 'datos_activacion_baja')
