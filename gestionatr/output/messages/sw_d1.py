# -*- coding: utf-8 -*-
from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera
from gestionatr.output.messages.sw_c1 import DatosInstGenCompleto


# Paso 01
class MensajeNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_cambios_atr_desde_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeNotificacionCambiosATRDesdeDistribuidor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_cambios_atr_desde_distribuidor = NotificacionCambiosATRDesdeDistribuidor()
        super(MensajeNotificacionCambiosATRDesdeDistribuidor, self) \
            .__init__('MensajeNotificacionCambiosATRDesdeDistribuidor', 'mensaje')


class NotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('notificacion_cambios_atr_desde_distribuidor', 'motivo_cambio_atr_desde_distribuidora',
                   'fecha_prevista_aplicacion_cambio_atr', 'periodicidad_facturacion', 'info_registro_autocons',
                   'info_retardo_activ_autocons_list')

    def __init__(self):
        self.notificacion_cambios_atr_desde_distribuidor = XmlField('NotificacionCambiosATRDesdeDistribuidor')
        self.motivo_cambio_atr_desde_distribuidora = XmlField('MotivoCambioATRDesdeDistribuidora')
        self.fecha_prevista_aplicacion_cambio_atr = XmlField('FechaPrevistaAplicacionCambioATR')
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')
        self.info_registro_autocons = InfoRegistroAutocons()
        self.info_retardo_activ_autocons_list = []
        super(NotificacionCambiosATRDesdeDistribuidor, self).__init__('NotificacionCambiosATRDesdeDistribuidor',
                                                                      'notificacion_cambios_atr_desde_distribuidor')


class InfoRegistroAutocons(XmlModel):

    _sort_order = ('info_registro_autocons', 'autoconsumo', 'datos_suministro', 'datos_inst_gen',
                   'comentarios')

    def __init__(self):
        self.info_registro_autocons = XmlField('InfoRegistroAutocons')
        self.autoconsumo = Autoconsumo()
        self.datos_suministro = DatosSuministro()
        self.datos_inst_gen = DatosInstGenCompleto()
        self.comentarios = XmlField('Comentarios')
        super(InfoRegistroAutocons, self).__init__('InfoRegistroAutocons', 'info_registro_autocons')


class Autoconsumo(XmlModel):

    _sort_order = ('autoconsumo', 'cau', 'seccion_registro', 'sub_seccion', 'colectivo')

    def __init__(self):
        self.autoconsumo = XmlField('Autoconsumo')
        self.cau = XmlField('CAU')
        self.seccion_registro = XmlField('SeccionRegistro')
        self.sub_seccion = XmlField('SubSeccion')
        self.colectivo = XmlField('Colectivo')
        super(Autoconsumo, self).__init__('Autoconsumo', 'autoconsumo')


class DatosSuministro(XmlModel):

    _sort_order = ('datos_suministro', 'cups', 'tipo_cups', 'ref_catastro')

    def __init__(self):
        self.datos_suministro = XmlField('DatosSuministro')
        self.cups = XmlField('CUPS')
        self.tipo_cups = XmlField('TipoCUPS')
        self.ref_catastro = XmlField('RefCatastro')
        super(DatosSuministro, self).__init__('DatosSuministro', 'datos_suministro')


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


# Paso 02 accept
class MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_notificacion_cambios_atr_desde_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_notificacion_cambios_atr_desde_distribuidor = AceptacionNotificacionCambiosATRDesdeDistribuidor()
        super(MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor, self)\
            .__init__('MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor', 'mensaje')


class AceptacionNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('aceptacion_notificacion_cambios_atr_desde_distribuidor', 'datos_aceptacion')

    def __init__(self):
        self.aceptacion_notificacion_cambios_atr_desde_distribuidor = XmlField('AceptacionNotificacionCambiosATRDesdeDistribuidor')
        self.datos_aceptacion = DatosAceptacion()
        super(AceptacionNotificacionCambiosATRDesdeDistribuidor, self)\
            .__init__('AceptacionNotificacionCambiosATRDesdeDistribuidor',
                      'aceptacion_notificacion_cambios_atr_desde_distribuidor')


class DatosAceptacion(XmlModel):

    _sort_order = ('datos_aceptacion', 'fecha_aceptacion')

    def __init__(self):
        self.datos_aceptacion = XmlField('DatosAceptacion')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        super(DatosAceptacion, self).__init__('DatosAceptacion', 'datos_aceptacion')


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
