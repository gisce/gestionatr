# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c1 import *


# Paso 01
class MensajeSolicitudAportacionLectura(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'datos_solicitud_aportacion_lectura', 'lectura_aportada_list')

    def __init__(self):
        self.mensaje = XmlField('MensajeSolicitudAportacionLectura',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.datos_solicitud_aportacion_lectura = DatosSolicitudAportacionLectura()
        self.lectura_aportada_list = []
        super(MensajeSolicitudAportacionLectura, self).__init__('MensajeSolicitudAportacionLectura', 'mensaje')


class DatosSolicitudAportacionLectura(XmlModel):

    _sort_order = ('datos_solicitud_aportacion_lectura', 'fecha_lectura', 'tipo_dhedm')

    def __init__(self):
        self.datos_solicitud_aportacion_lectura = XmlField('DatosSolicitudAportacionLectura')
        self.fecha_lectura = XmlField('FechaLectura')
        self.tipo_dhedm = XmlField('TipoDHEdM')
        super(DatosSolicitudAportacionLectura, self).__init__('DatosSolicitudAportacionLectura', 'datos_solicitud_aportacion_lectura')


class LecturaAportada(XmlModel):

    _sort_order = ('lectura_aportada', 'integrador', 'tipo_codigo_periodo_dh', 'lectura_propuesta')

    def __init__(self):
        self.lectura_aportada = XmlField('LecturaAportada')
        self.integrador = XmlField('Integrador')
        self.tipo_codigo_periodo_dh = XmlField('TipoCodigoPeriodoDH')
        self.lectura_propuesta = XmlField('LecturaPropuesta')
        super(LecturaAportada, self).__init__('LecturaAportada', 'lectura_aportada')


# Paso 02
class AceptacionAportacionLectura(XmlModel):
    _sort_order = (
    'aceptacion_aportacion_lectura', 'cabecera', 'datos_aceptacion_lectura')

    def __init__(self):
        self.mensaje = XmlField('AceptacionAportacionLectura',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.datos_aceptacion_lectura = DatosAceptacionLectura()
        super(AceptacionAportacionLectura, self).__init__('AceptacionAportacionLectura', 'mensaje')


class DatosAceptacionLectura(XmlModel):

    _sort_order = ('datos_aceptacion_lectura', 'fecha_aceptacion')

    def __init__(self):
        self.datos_aceptacion_lectura = XmlField('DatosAceptacionLectura')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        super(DatosAceptacionLectura, self).__init__('DatosAceptacionLectura', 'datos_aceptacion_lectura')
