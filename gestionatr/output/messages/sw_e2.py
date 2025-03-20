# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c2 import *
from gestionatr.output.messages.sw_c1 import Medida, Contrato
from gestionatr.output.messages.sw_t1 import DireccionPS

# Paso 01

class MensajeSolicitudReposicion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'solicitud_reposicion')

    def __init__(self):
        self.mensaje = XmlField('MensajeSolicitudReposicion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.solicitud_reposicion = SolicitudReposicion()
        super(MensajeSolicitudReposicion, self).__init__('MensajeSolicitudReposicion', 'mensaje')


class SolicitudReposicion(XmlModel):

    _sort_order = ('solicitud_reposicion', 'codigo_de_solicitud_ref',
                   'tipo_de_reposicion', 'id_cliente', 'registros_documento', 'comentarios')

    def __init__(self):
        self.solicitud_reposicion = XmlField('SolicitudReposicion')
        self.codigo_de_solicitud_ref = XmlField('CodigoDeSolicitudRef')
        self.tipo_de_reposicion = XmlField('TipoDeReposicion')
        self.id_cliente = IdCliente()
        self.registros_documento = RegistrosDocumento()
        self.comentarios = XmlField('Comentarios')
        super(SolicitudReposicion, self).__init__('SolicitudReposicion', 'solicitud_reposicion')


# Paso 02

class MensajeAceptacionReposicion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_reposicion')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionReposicion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_reposicion = AceptacionReposicion()
        super(MensajeAceptacionReposicion, self).__init__('MensajeAceptacionReposicion', 'mensaje')


class AceptacionReposicion(XmlModel):

    _sort_order = ('aceptacion_reposicion', 'fecha_aceptacion',
                   'actuacion_campo', 'fecha_activacion_prevista')

    def __init__(self):
        self.aceptacion_reposicion = XmlField('AceptacionReposicion')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        self.actuacion_campo = XmlField('ActuacionCampo')
        self.fecha_activacion_prevista = XmlField('FechaActivacionPrevista')
        super(AceptacionReposicion, self).__init__('AceptacionReposicion', 'aceptacion_reposicion')


# Paso 05

class MensajeActivacionReposicion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_reposicion')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionReposicion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_reposicion = ActivacionReposicion()
        super(MensajeActivacionReposicion, self).__init__('MensajeActivacionReposicion', 'mensaje')


class ActivacionReposicion(XmlModel):

    _sort_order = ('activacion_reposicion', 'datos_notificacion', 'contrato', 'puntos_de_medida',
                   'id_cliente', 'registros_documento', 'comentarios')

    def __init__(self):
        self.activacion_reposicion = XmlField('ActivacionReposicion')
        self.datos_notificacion = DatosNotificacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        self.id_cliente = IdCliente()
        self.registros_documento = RegistrosDocumento()
        self.comentarios = XmlField('Comentarios')
        super(ActivacionReposicion, self).__init__('ActivacionReposicion', 'activacion_reposicion')


class DatosNotificacion(XmlModel):

    _sort_order = ('datos_notificacion', 'fecha_activacion', 'resultado_activacion', 'codigo_sol_corte',
                   'ind_esencial', 'fecha_ultimo_movimiento_ind_esencial')

    def __init__(self):
        self.datos_notificacion = XmlField('DatosNotificacion')
        self.fecha_activacion = XmlField('FechaActivacion')
        self.resultado_activacion = XmlField('ResultadoActivacion')
        self.codigo_sol_corte = XmlField('CodigoSolCorte')
        self.ind_esencial = XmlField('IndEsencial')
        self.fecha_ultimo_movimiento_ind_esencial = XmlField('FechaUltimoMovimientoIndEsencial')
        super(DatosNotificacion, self).__init__('DatosNotificacion', 'datos_notificacion')


# Paso 06
class MensajeNotificacionActivacionPorReposicion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_activacion_reposicion')

    def __init__(self):
        self.mensaje = XmlField('MensajeNotificacionActivacionPorReposicion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_activacion_reposicion = NotificacionActivacionPorReposicion()
        super(MensajeNotificacionActivacionPorReposicion, self)\
            .__init__('MensajeNotificacionActivacionPorReposicion', 'mensaje')


class NotificacionActivacionPorReposicion(XmlModel):

    _sort_order = ('notificacion_activacion_reposicion', 'datos_activacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.notificacion_activacion_reposicion = XmlField('NotificacionActivacionPorReposicion')
        self.datos_activacion = DatosActivacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(NotificacionActivacionPorReposicion, self).__init__('NotificacionActivacionPorReposicion',
                                                                     'notificacion_activacion_reposicion')


class DatosActivacion(XmlModel):

    _sort_order = ('datos_activacion', 'fecha', 'resultado_activacion', 'en_servicio',)

    def __init__(self):
        self.datos_activacion = XmlField('DatosActivacion')
        self.fecha = XmlField('Fecha')
        self.resultado_activacion = XmlField('ResultadoActivacion')
        self.en_servicio = XmlField('EnServicio')
        super(DatosActivacion, self).__init__('DatosActivacion', 'datos_activacion')


class Medida(Medida):

    _sort_order = ('medida', 'tipo_dhedm', 'periodo', 'magnitud_medida', 'procedencia', 'ultima_lectura_firme',
                   'fecha_lectura_firme', 'anomalia', 'comentarios')

    def __init__(self):
        super(Medida, self).__init__()


class Contrato(Contrato):

    _sort_order = ('contrato', 'id_contrato', 'autoconsumo', 'tipo_contrato_atr', 'cups_principal',
                   'condiciones_contractuales')

    def __init__(self):
        super(Contrato, self).__init__()
        self.cups_principal = XmlField('CUPSPrincipal')

# Paso 12

class MensajeRechazoReposicion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'rechazo_reposicion')

    def __init__(self):
        self.mensaje = XmlField('MensajeRechazoReposicion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazo_reposicion = RechazoReposicion()
        super(MensajeRechazoReposicion, self).__init__('MensajeRechazoReposicion', 'mensaje')


class RechazoReposicion(XmlModel):

    _sort_order = ('rechazo_reposicion', 'fecha_rechazo')

    def __init__(self):
        self.rechazo_reposicion = XmlField('RechazoReposicion')
        self.fecha_rechazo = XmlField('FechaRechazo')
        super(RechazoReposicion, self).__init__('RechazoReposicion', 'rechazo_reposicion')


# paso 14
class MensajeConsultaSolicitudReposicion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'solicitud_reposicion', 'direccion_ps', 'registros_documentos')

    def __init__(self):
        self.mensaje = XmlField('MensajeConsultaSolicitudReposicion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.solicitud_reposicion = SolicitudReposicionConsulta()
        self.direccion_ps = DireccionPS()
        self.registros_documentos = RegistrosDocumento()
        super(MensajeConsultaSolicitudReposicion, self).__init__('MensajeConsultaSolicitudReposicion', 'mensaje')


class SolicitudReposicionConsulta(XmlModel):

    _sort_order = ('solicitud_reposicion_consulta', 'codigo_de_solicitud_ref',
                   'tipo_de_reposicion', 'fecha_prevista_accion', 'actuacion_campo')

    def __init__(self):
        self.solicitud_reposicion_consulta = XmlField('SolicitudReposicion')
        self.codigo_de_solicitud_ref = XmlField('CodigoDeSolicitudRef')
        self.tipo_de_reposicion = XmlField('TipoDeReposicion')
        self.fecha_prevista_accion = XmlField('FechaPrevistaAccion')
        self.actuacion_campo = XmlField('ActuacionCampo')

        super(SolicitudReposicionConsulta, self).__init__('SolicitudReposicionConsulta',
                                                          'solicitud_reposicion_consulta')

# Paso 15

class MensajeAceptacionReposicionReceptor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_reposicion_receptor')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionReposicionReceptor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_reposicion_receptor = AceptacionReposicionReceptor()
        super(MensajeAceptacionReposicionReceptor, self).__init__('MensajeAceptacionReposicionReceptor', 'mensaje')


class AceptacionReposicionReceptor(XmlModel):

    _sort_order = ('aceptacion_reposicion_receptor', 'aceptacion_reposicion')

    def __init__(self):
        self.aceptacion_reposicion_receptor = XmlField('AceptacionReposicionReceptor')
        self.aceptacion_reposicion = XmlField('AceptacionReposicion')
        super(AceptacionReposicionReceptor, self).__init__('AceptacionReposicionReceptor', 'aceptacion_reposicion_receptor')

class MensajeRechazoReposicionReceptor(XmlModel):

    _sort_order = ('mensaje_rechazo', 'cabecera', 'rechazos',
                   'registros_documentos')

    def __init__(self):
        self.mensaje_rechazo = XmlField('MensajeRechazoReposicionReceptor',
                                        attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazos = Rechazos()
        self.registros_documentos = RegistrosDocumento()
        super(MensajeRechazoReposicionReceptor, self).__init__('MensajeRechazoReposicionReceptor', 'mensaje_rechazo')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'fecha_rechazo', 'rechazo_list')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.rechazo_list = []
        super(Rechazos, self).__init__('Rechazos', 'rechazos')