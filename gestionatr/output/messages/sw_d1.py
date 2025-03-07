# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera
from gestionatr.output.messages.sw_c1 import Autoconsumo


# Paso 01
class MensajeNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_cambios_atr_desde_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeNotificacionCambiosATRDesdeDistribuidor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_cambios_atr_desde_distribuidor = []
        super(MensajeNotificacionCambiosATRDesdeDistribuidor, self) \
            .__init__('MensajeNotificacionCambiosATRDesdeDistribuidor', 'mensaje')


class NotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('notificacion_cambios_atr_desde_distribuidor', 'motivo_cambio_atr_desde_distribuidora',
                   'fecha_prevista_aplicacion_cambio_atr', 'fecha_maxima_rechazo', 'periodicidad_facturacion',
                   'ind_esencial', 'fecha_ultimo_movimiento_ind_esencial', 'info_registro_autocons',
                   'info_retardo_activ_autocons_list', 'registros_documento')

    def __init__(self):
        self.notificacion_cambios_atr_desde_distribuidor = XmlField('NotificacionCambiosATRDesdeDistribuidor')
        self.motivo_cambio_atr_desde_distribuidora = XmlField('MotivoCambioATRDesdeDistribuidora')
        self.fecha_prevista_aplicacion_cambio_atr = XmlField('FechaPrevistaAplicacionCambioATR')
        self.fecha_maxima_rechazo = XmlField('FechaMaximaRechazo')
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')
        self.ind_esencial = XmlField('IndEsencial')
        self.fecha_ultimo_movimiento_ind_esencial = XmlField('FechaUltimoMovimientoIndEsencial')
        self.info_registro_autocons = InfoRegistroAutocons()
        self.info_retardo_activ_autocons_list = []
        self.registros_documento = RegistrosDocumento()
        super(NotificacionCambiosATRDesdeDistribuidor, self).__init__('NotificacionCambiosATRDesdeDistribuidor',
                                                                      'notificacion_cambios_atr_desde_distribuidor')


class InfoRegistroAutocons(XmlModel):

    _sort_order = ('info_registro_autocons', 'autoconsumo')

    def __init__(self):
        self.info_registro_autocons = XmlField('InfoRegistroAutocons')
        self.autoconsumo = Autoconsumo()
        super(InfoRegistroAutocons, self).__init__('InfoRegistroAutocons', 'info_registro_autocons')

class InfoRetardoActivAutocons(XmlModel):

    _sort_order = ('info_retardo_activ_autocons', 'codigo_fiscal_factura', 'fecha_inicio_conteo_activ_autocons',
                   'fecha_desde', 'fecha_hasta', 'dias_retardo_activ_autocons', 'valor_energia_anual_calculada',
                   'valor_energia_horaria_calculada', 'pot_instalada_gen')
    def __init__(self):
        self.info_retardo_activ_autocons = XmlField('InfoRetardoActivAutocons')
        self.codigo_fiscal_factura = XmlField('CodigoFiscalFactura')
        self.fecha_inicio_conteo_activ_autocons = XmlField('FechaInicioConteoActivAutocons')
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.dias_retardo_activ_autocons = XmlField('DiasRetardoActivAutocons')
        self.valor_energia_anual_calculada = XmlField('ValorEnergiaAnualCalculada')
        self.valor_energia_horaria_calculada = XmlField('ValorEnergiaHorariaCalculada')
        self.pot_instalada_gen = XmlField('PotInstaladaGen')
        super(InfoRetardoActivAutocons, self).__init__('InfoRetardoActivAutocons', 'info_retardo_activ_autocons')


# Paso 02 (Rechazo)
class MensajeRechazo(XmlModel):

    _sort_order = ('mensaje_rechazo', 'cabecera', 'rechazos')

    def __init__(self):
        self.mensaje_rechazo = XmlField('MensajeRechazoD1',
                                        attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazos = Rechazos()
        super(MensajeRechazo, self).__init__('MensajeRechazo', 'mensaje_rechazo')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'fecha_rechazo', 'rechazo', 'registros_documento')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.rechazo = Rechazo()
        self.registros_documento = RegistrosDocumento()
        super(Rechazos, self).__init__('Rechazos', 'rechazos')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'secuencial', 'codigo_motivo', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')


class RegistrosDocumento(XmlModel):

    _sort_order = ('registros_documento', 'registro_doc')

    def __init__(self):
        self.registros_documento = XmlField('RegistrosDocumento')
        self.registro_doc = RegistroDoc()
        super(RegistrosDocumento, self).__init__('RegistrosDocumento', 'registros_documento')


class RegistroDoc(XmlModel):

    _sort_order = ('registro_doc', 'tipo_doc_aportado', 'direccion_url')

    def __init__(self):
        self.registro_doc = XmlField('RegistroDoc')
        self.tipo_doc_aportado = XmlField('TipoDocAportado')
        self.direccion_url = XmlField('DireccionUrl')
        super(RegistroDoc, self).__init__('RegistroDoc', 'registro_doc')


# Paso 10
class MensajeAnulacionD1(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'anulacion_notificacion_cambios_atr_desde_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeAnulacionD1', attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.anulacion_notificacion_cambios_atr_desde_distribuidor = AnulacionNotificacionCambiosATRDesdeDistribuidor()
        super(MensajeAnulacionD1, self).__init__('MensajeAnulacionD1', 'mensaje')


class AnulacionNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('anulacion_notificacion_cambios_atr_desde_distribuidor', 'datos_anulacion')

    def __init__(self):
        self.anulacion_notificacion_cambios_atr_desde_distribuidor = XmlField(
            'AnulacionNotificacionCambiosATRDesdeDistribuidor'
        )
        self.datos_anulacion = DatosAnulacion()
        super(AnulacionNotificacionCambiosATRDesdeDistribuidor, self).__init__(
            'AnulacionNotificacionCambiosATRDesdeDistribuidor', 'anulacion_notificacion_cambios_atr_desde_distribuidor'
        )


class DatosAnulacion(XmlModel):

    _sort_order = ('datos_anulacion', 'fecha_anulacion')

    def __init__(self):
        self.datos_anulacion = XmlField('DatosAnulacion')
        self.fecha_anulacion = XmlField('FechaAnulacion')
        super(DatosAnulacion, self).__init__('DatosAnulacion', 'datos_anulacion')
