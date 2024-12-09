# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gestionatr.output.messages.sw_m1 import *

# Paso 02 -> C1 MensajeRechazo


# Paso 05
class MensajeActivacionModificacionDeATRUnidir(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_modificaciones')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionModificacionDeATRUnidir',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_modificaciones = ActivacionModificaciones()
        super(MensajeActivacionModificacionDeATRUnidir, self).__init__(
            'MensajeActivacionModificacionDeATRUnidir', 'mensaje'
        )


class ActivacionModificaciones(XmlModel):

    _sort_order = ('activacion_modificaciones', 'datos_activacion', 'ind_esencial',
                   'fecha_ultimo_movimiento_ind_esencial', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_modificaciones = XmlField('ActivacionModificaciones')
        self.datos_activacion = DatosActivacion()
        self.ind_esencial = XmlField('IndEsencial')
        self.fecha_ultimo_movimiento_ind_esencial = XmlField('FechaUltimoMovimientoIndEsencial')
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionModificaciones, self).__init__('ActivacionModificaciones', 'activacion_modificaciones')


class DatosActivacion(DatosActivacion):

    _sort_order = ('datos_activacion', 'motivo_activacion_list', 'fecha', 'bono_social', 'ind_esencial',
                   'fecha_ultimo_movimiento_ind_esencial')

    def __init__(self):
        super(DatosActivacion, self).__init__()
        self.motivo_activacion_list = []


class MotivoActivacionUnidireccional(XmlModel):

    _sort_order = ('motivo_activacion_unidireccional', 'motivo')

    def __init__(self):
        self.motivo_activacion_unidireccional = XmlField('MotivoActivacionUnidireccional')
        self.motivo = XmlField('Motivo')
        super(MotivoActivacionUnidireccional, self).__init__(
            'MotivoActivacionUnidireccional', 'motivo_activacion_unidireccional'
        )
