# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c2 import *
from gestionatr.output.messages.sw_c1 import Medida, Contrato

# Paso 01

class MensajeSolicitudDesistimiento(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'solicitud_desistimiento')

    def __init__(self):
        self.mensaje = XmlField('MensajeSolicitudDesistimiento',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.solicitud_desistimiento = SolicitudDesistimiento()
        super(MensajeSolicitudDesistimiento, self) \
            .__init__('MensajeSolicitudDesistimiento', 'mensaje')


class SolicitudDesistimiento(XmlModel):

    _sort_order = ('solicitud_desistimiento', 'codigo_de_solicitud_ref',
                   'tipo_de_solicitud', 'id_cliente', 'registros_Documento')

    def __init__(self):
        self.solicitud_desistimiento = XmlField('SolicitudDesistimiento')
        self.codigo_de_solicitud_ref = XmlField('CodigoDeSolicitudRef')
        self.tipo_de_solicitud = XmlField('TipoDeSolicitud')
        self.id_cliente = IdCliente()
        self.registros_Documento = RegistrosDocumento()
        super(SolicitudDesistimiento, self).__init__('SolicitudDesistimiento', 'solicitud_desistimiento')


# Paso 02

class MensajeAceptacionDesistimiento(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_desistimiento')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionDesistimiento',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_desistimiento = AceptacionDesistimiento()
        super(MensajeAceptacionDesistimiento, self).__init__('MensajeAceptacionDesistimiento', 'mensaje')


class AceptacionDesistimiento(XmlModel):

    _sort_order = ('aceptacion_desistimiento', 'fecha_aceptacion',
                   'ind_anulable', 'actuacion_campo', 'fecha_activacion_prevista')

    def __init__(self):
        self.aceptacion_desistimiento = XmlField('AceptacionDesistimiento')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        self.ind_anulable = XmlField('IndAnulable')
        self.actuacion_campo = XmlField('ActuacionCampo')
        self.fecha_activacion_prevista = XmlField('FechaActivacionPrevista')
        super(AceptacionDesistimiento, self).__init__('AceptacionDesistimiento', 'aceptacion_desistimiento')


# Paso 05

class MensajeActivacionDesistimiento(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_desistimiento')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionDesistimiento',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_desistimiento = ActivacionDesistimiento()
        super(MensajeActivacionDesistimiento, self).__init__('MensajeActivacionDesistimiento', 'mensaje')


class ActivacionDesistimiento(XmlModel):

    _sort_order = ('activacion_desistimiento', 'datos_notificacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_desistimiento = XmlField('ActivacionDesistimiento')
        self.datos_notificacion = DatosNotificacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionDesistimiento, self).__init__('ActivacionDesistimiento', 'activacion_desistimiento')


class DatosNotificacion(DatosNotificacion):

    _sort_order = ('datos_notificacion', 'fecha_activacion', 'resultado_activacion', 'ind_anulable')

    def __init__(self):
        super(DatosNotificacion, self).__init__()
        self.resultado_activacion = XmlField('ResultadoActivacion')
        self.ind_anulable = XmlField('IndAnulable')


# Paso 06

class MensajeNotificacionActivacionPorDesistimiento(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_activacion_desistimiento')

    def __init__(self):
        self.mensaje = XmlField('MensajeNotificacionActivacionPorDesistimiento',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_activacion_desistimiento = NotificacionActivacionPorDesistimiento()
        super(MensajeNotificacionActivacionPorDesistimiento, self)\
            .__init__('MensajeNotificacionActivacionPorDesistimiento', 'mensaje')


class NotificacionActivacionPorDesistimiento(XmlModel):

    _sort_order = ('notificacion_activacion_desistimiento', 'datos_activacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.notificacion_activacion_desistimiento = XmlField('NotificacionActivacionPorDesistimiento')
        self.datos_activacion = DatosActivacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(NotificacionActivacionPorDesistimiento, self).__init__('NotificacionActivacionPorDesistimiento',
                                                                     'notificacion_activacion_desistimiento')


class DatosActivacion(DatosActivacion):

    _sort_order = ('datos_activacion', 'fecha', 'en_servicio', 'ind_anulable')

    def __init__(self):
        super(DatosActivacion, self).__init__()
        self.en_servicio = XmlField('EnServicio')
        self.ind_anulable = XmlField('IndAnulable')


class Medida(Medida):

    _sort_order = ('medida', 'tipo_dhedm', 'periodo', 'magnitud_medida', 'procedencia', 'ultima_lectura_firme',
                   'fecha_lectura_firme', 'anomalia', 'comentarios')

    def __init__(self):
        super(Medida, self).__init__()


class Contrato(Contrato):

    _sort_order = ('contrato', 'id_contrato', 'tipo_autoconsumo', 'tipo_contrato_atr', 'condiciones_contractuales')

    def __init__(self):
        super(Contrato, self).__init__()


# Paso 12

class MensajeRechazoDesistimiento(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'rechazo_desistimiento')

    def __init__(self):
        self.mensaje = XmlField('MensajeRechazoDesistimiento',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazo_desistimiento = RechazoDesistimiento()
        super(MensajeRechazoDesistimiento, self).__init__('MensajeRechazoDesistimiento', 'mensaje')


class RechazoDesistimiento(XmlModel):

    _sort_order = ('rechazo_desistimiento', 'fecha_rechazo')

    def __init__(self):
        self.rechazo_desistimiento = XmlField('RechazoDesistimiento')
        self.fecha_rechazo = XmlField('FechaRechazo')
        super(RechazoDesistimiento, self).__init__('RechazoDesistimiento', 'rechazo_desistimiento')



