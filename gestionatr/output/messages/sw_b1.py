# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c2 import *


# Paso 01
class MensajeBajaSuspension(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'baja_suspension')

    def __init__(self):
        self.mensaje = XmlField('MensajeBajaSuspension',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.baja_suspension = BajaSuspension()
        super(MensajeBajaSuspension, self).__init__('MensajeBajaSuspension', 'mensaje')


class BajaSuspension(XmlModel):

    _sort_order = ('baja_suspension', 'datos_solicitud', 'cliente', 'contacto', 'iban', 'comentarios', 'registros_documento')

    def __init__(self):
        self.baja_suspension = XmlField('BajaSuspension')
        self.datos_solicitud = DatosSolicitud()
        self.cliente = Cliente()
        self.contacto = Contacto()
        self.iban = XmlField('IBAN')
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(BajaSuspension, self).__init__('BajaSuspension', 'baja_suspension')


class DatosSolicitud(DatosSolicitud):

    _sort_order = ('datos_solicitud', 'tipo_modificacion', 'tipo_solicitud_administrativa', 'cnae', 'ind_activacion', 'fecha_prevista_accion', 'motivo', 'contratacion_incondicional_ps')

    def __init__(self):
        super(DatosSolicitud, self).__init__()
        self.motivo = XmlField('Motivo')


# Paso 02
class MensajeAceptacionBajaSuspension(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_baja_suspension')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionBajaSuspension',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_baja_suspension = AceptacionBajaSuspension()
        super(MensajeAceptacionBajaSuspension, self).__init__('MensajeAceptacionBajaSuspension', 'mensaje')


class AceptacionBajaSuspension(XmlModel):

    _sort_order = ('aceptacion_baja_suspension', 'datos_aceptacion')

    def __init__(self):
        self.aceptacion_baja_suspension = XmlField('AceptacionBajaSuspension')
        self.datos_aceptacion = DatosAceptacion()
        super(AceptacionBajaSuspension, self).__init__('AceptacionBajaSuspension', 'aceptacion_baja_suspension')


class DatosAceptacion(DatosAceptacion):

    _sort_order = ('datos_aceptacion', 'fecha_aceptacion', 'potencia_actual', 'actuacion_campo', 'fecha_ultima_lectura_firme', 'tipo_activacion_prevista', 'fecha_activacion_prevista')

    def __init__(self):
        super(DatosAceptacion, self).__init__()
        self.tipo_activacion_prevista = XmlField('TipoActivacionPrevista')
        self.fecha_activacion_prevista = XmlField('FechaActivacionPrevista')


# Paso 03 -> C1 MensajeAnulacionSolicitud

# Paso 04
class MensajeAceptacionAnulacionBaja(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_anulacion')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionAnulacionBaja',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_anulacion = AceptacionAnulacion()
        super(MensajeAceptacionAnulacionBaja, self).__init__('MensajeAceptacionAnulacionBaja', 'mensaje')


class AceptacionAnulacion(AceptacionAnulacion):

    _sort_order = ('aceptacion_anulacion', 'fecha_aceptacion', 'hora_aceptacion')

    def __init__(self):
        super(AceptacionAnulacion, self).__init__()
        self.hora_aceptacion = XmlField('HoraAceptacion')


# Paso 05
class MensajeActivacionBajaSuspension(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_baja')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionBajaSuspension',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_baja = ActivacionBaja()
        super(MensajeActivacionBajaSuspension, self).__init__('MensajeActivacionBajaSuspension', 'mensaje')


class ActivacionBaja(XmlModel):

    _sort_order = ('activacion_baja', 'datos_activacion_baja', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_baja = XmlField('ActivacionBaja')
        self.datos_activacion_baja = DatosActivacionBaja()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionBaja, self).__init__('ActivacionBaja', 'activacion_baja')


class DatosActivacionBaja(XmlModel):

    _sort_order = ('datos_activacion_baja', 'fecha_activacion')

    def __init__(self):
        self.datos_activacion_baja = XmlField('DatosActivacionBaja')
        self.fecha_activacion = XmlField('FechaActivacion')
        super(DatosActivacionBaja, self).__init__('DatosActivacionBaja', 'datos_activacion_baja')

# Paso 06 -> C2 MensajeIncidenciasATRDistribuidor
# Paso 07 -> C1 MensajeRechazo
