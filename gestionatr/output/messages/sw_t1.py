# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c2 import *
from gestionatr.output.messages.sw_c1 import Medida
from gestionatr.output.messages.sw_f1 import DireccionSuministro


# Paso 01

class MensajeSolicitudTraspasoCOR(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'solicitud_traspaso_cor')

    def __init__(self):
        self.mensaje = XmlField('MensajeSolicitudTraspasoCOR',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.solicitud_traspaso_cor = SolicitudTraspasoCOR()
        super(MensajeSolicitudTraspasoCOR, self) \
            .__init__('MensajeSolicitudTraspasoCOR', 'mensaje')


class SolicitudTraspasoCOR(XmlModel):

    _sort_order = ('solicitud_traspaso_cor', 'datos_solicitud', 'contrato', 'cliente',
                   'direccion_ps', 'registros_documento')

    def __init__(self):
        self.solicitud_traspaso_cor = XmlField('SolicitudTraspasoCOR')
        self.datos_solicitud = DatosSolicitud()
        self.contrato = ContratoT101()
        self.cliente = Cliente()
        self.direccion_ps = DireccionPS()
        self.registros_documento = RegistrosDocumento()
        super(SolicitudTraspasoCOR, self).__init__('SolicitudTraspasoCOR', 'solicitud_traspaso_cor')


class DatosSolicitud(XmlModel):

    _sort_order = ('datos_solicitud', 'motivo_traspaso', 'fecha_prevista_accion', 'cnae',
                   'ind_esencial', 'susp_baja_impago_en_curso')

    def __init__(self):
        self.datos_solicitud = XmlField('DatosSolicitud')
        self.motivo_traspaso = XmlField('MotivoTraspaso')
        self.fecha_prevista_accion = XmlField('FechaPrevistaAccion')
        self.cnae = XmlField('CNAE')
        self.ind_esencial = XmlField('IndEsencial')
        self.susp_baja_impago_en_curso = XmlField('SuspBajaImpagoEnCurso')

        super(DatosSolicitud, self).__init__('DatosSolicitud', 'datos_solicitud')


class ContratoT101(Contrato):

    _sort_order = ('contrato', 'fecha_finalizacion', 'tipo_autoconsumo', 'tipo_contrato_atr',
                   'condiciones_contractuales', 'periodicidad_facturacion', 'consumo_anual_estimado', 'contacto')

    def __init__(self):
        super(ContratoT101, self).__init__()


class DireccionPS(DireccionSuministro):

    _sort_order = ('direccion', 'pais', 'provincia', 'municipio', 'poblacion', 'tipo_via', 'cod_postal',
                   'calle', 'numero_finca', 'duplicador_finca', 'escalera', 'piso', 'puerta',
                   'tipo_aclarador_finca', 'aclarador_finca')

    def __init__(self, name='DireccionPS'):
        super(DireccionPS, self).__init__(name=name)


# Paso 02

class MensajeAceptacionTraspasoCOR(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_traspaso_cor')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionTraspasoCOR',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_traspaso_cor = AceptacionTraspasoCOR()
        super(MensajeAceptacionTraspasoCOR, self).__init__('MensajeAceptacionTraspasoCOR', 'mensaje')


class MensajeRechazoTraspasoCOR(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'rechazos')

    def __init__(self):
        self.mensaje = XmlField('MensajeRechazoTraspasoCOR',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazos = Rechazos()
        super(MensajeRechazoTraspasoCOR, self).__init__('MensajeRechazoTraspasoCOR', 'mensaje')


class AceptacionTraspasoCOR(XmlModel):

    _sort_order = ('aceptacion_traspaso_cor', 'datos_aceptacion')

    def __init__(self):
        self.aceptacion_traspaso_cor = XmlField('AceptacionTraspasoCOR')
        self.datos_aceptacion = DatosAceptacion()
        super(AceptacionTraspasoCOR, self).__init__('AceptacionTraspasoCOR', 'aceptacion_traspaso_cor')


class DatosAceptacion(DatosAceptacion):

    _sort_order = ('datos_aceptacion', 'fecha_aceptacion')

    def __init__(self):
        super(DatosAceptacion, self).__init__()


# Paso 05

class MensajeActivacionTraspasoCOR(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_traspaso_cor')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionTraspasoCOR',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_traspaso_cor = ActivacionTraspasoCOR()
        super(MensajeActivacionTraspasoCOR, self).__init__('MensajeActivacionTraspasoCOR', 'mensaje')


class ActivacionTraspasoCOR(XmlModel):

    _sort_order = ('activacion_traspaso_cor', 'datos_activacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_traspaso_cor = XmlField('ActivacionTraspasoCOR')
        self.datos_activacion = DatosActivacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionTraspasoCOR, self).__init__('ActivacionTraspasoCOR', 'activacion_traspaso_cor')


class DatosActivacion(XmlModel):

    _sort_order = ('datos_activacion', 'fecha_activacion', 'en_servicio')

    def __init__(self):
        self.datos_activacion = XmlField('DatosActivacion')
        self.fecha_activacion = XmlField('FechaActivacion')
        self.en_servicio = XmlField('EnServicio')
        super(DatosActivacion, self).__init__('DatosActivacion', 'datos_activacion')


# Paso 06

class MensajeActivacionTraspasoCORSaliente(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_comercializador_saliente_t1')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionComercializadorSalienteT1',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_comercializador_saliente_t1 = NotificacionComercializadorSalienteT1()
        super(MensajeActivacionTraspasoCORSaliente, self).__init__('MensajeActivacionTraspasoCORSalienteT1', 'mensaje')


class NotificacionComercializadorSalienteT1(XmlModel):

    _sort_order = ('notificacion_comercializador_saliente_t1', 'datos_notificacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.notificacion_comercializador_saliente_t1 = XmlField('NotificacionComercializadorSalienteT1')
        self.datos_notificacion = DatosNotificacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(NotificacionComercializadorSalienteT1, self).__init__('NotificacionComercializadorSalienteT1', 'notificacion_comercializador_saliente_t1')


class Medida(Medida):

    _sort_order = ('medida', 'tipo_dhedm', 'periodo', 'magnitud_medida', 'procedencia', 'ultima_lectura_firme',
                   'fecha_lectura_firme', 'anomalia', 'comentarios')

    def __init__(self):
        super(Medida, self).__init__()



