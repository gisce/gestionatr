# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera


# Paso 01
class MensajeNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_cambios_atr_desde_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeNotificacionCambiosATRDesdeDistribuidor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_cambios_atr_desde_distribuidor = NotificacionCambiosATRDesdeDistribuidor()
        super(MensajeNotificacionCambiosATRDesdeDistribuidor, self).__init__('MensajeNotificacionCambiosATRDesdeDistribuidor', 'mensaje')


class NotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('notificacion_cambios_atr_desde_distribuidor', 'motivo_cambio_atr_desde_distribuidora', 'fecha_prevista_aplicacion_cambio_atr', 'periodicidad_facturacion')

    def __init__(self):
        self.notificacion_cambios_atr_desde_distribuidor = XmlField('NotificacionCambiosATRDesdeDistribuidor')
        self.motivo_cambio_atr_desde_distribuidora = XmlField('MotivoCambioATRDesdeDistribuidora')
        self.fecha_prevista_aplicacion_cambio_atr = XmlField('FechaPrevistaAplicacionCambioATR')
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')
        super(NotificacionCambiosATRDesdeDistribuidor, self).__init__('NotificacionCambiosATRDesdeDistribuidor', 'notificacion_cambios_atr_desde_distribuidor')
