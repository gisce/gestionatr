# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c2 import *


# Paso 01
class MensajeModificacionDeATR(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'modificacion_de_atr')

    def __init__(self):
        self.mensaje = XmlField('MensajeModificacionDeATR',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.modificacion_de_atr = ModificacionDeATR()
        super(MensajeModificacionDeATR, self).__init__('MensajeModificacionDeATR', 'mensaje')


class ModificacionDeATR(XmlModel):

    _sort_order = ('modificacion_de_atr', 'datos_solicitud', 'contrato', 'cliente', 'medida', 'doc_tecnica', 'comentarios', 'registros_documento')

    def __init__(self):
        self.modificacion_de_atr = XmlField('ModificacionDeATR')
        self.datos_solicitud = DatosSolicitud()
        self.contrato = Contrato()
        self.cliente = Cliente()
        self.medida = Medida()
        self.doc_tecnica = DocTecnica()
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(ModificacionDeATR, self).__init__('ModificacionDeATR', 'modificacion_de_atr')


class DatosSolicitud(DatosSolicitud):

    _sort_order = ('datos_solicitud', 'tipo_modificacion', 'tipo_solicitud_administrativa', 'periodicidad_facturacion', 'ind_activacion', 'fecha_prevista_accion', 'cnae', 'contratacion_incondicional_ps')

    def __init__(self):
        super(DatosSolicitud, self).__init__()
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')


# Paso 02
class MensajeAceptacionModificacionDeATR(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_modificacion_de_atr')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionModificacionDeATR',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_modificacion_de_atr = AceptacionModificacionDeATR()
        super(MensajeAceptacionModificacionDeATR, self).__init__('MensajeAceptacionModificacionDeATR', 'mensaje')


class AceptacionModificacionDeATR(XmlModel):

    _sort_order = ('aceptacion_modificacion_de_atr', 'datos_aceptacion', 'contrato')

    def __init__(self):
        self.aceptacion_modificacion_de_atr = XmlField('AceptacionModificacionDeATR')
        self.datos_aceptacion = DatosAceptacion()
        self.contrato = Contrato()
        super(AceptacionModificacionDeATR, self).__init__('AceptacionModificacionDeATR', 'aceptacion_modificacion_de_atr')


# Paso 03 -> C2 MensajeIncidenciasATRDistribuidor
# Paso 04 -> C1 MensajeRechazo

# Paso 05
class MensajeActivacionModificacionDeATR(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_modificaciones')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionModificacionDeATR',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_modificaciones = ActivacionModificaciones()
        super(MensajeActivacionModificacionDeATR, self).__init__('MensajeActivacionModificacionDeATR', 'mensaje')


class ActivacionModificaciones(XmlModel):

    _sort_order = ('activacion_modificaciones', 'datos_activacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_modificaciones = XmlField('ActivacionModificaciones')
        self.datos_activacion = DatosActivacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionModificaciones, self).__init__('ActivacionModificaciones', 'activacion_modificaciones')


# Paso 06 -> C1 MensajeAnulacionSolicitud
# Paso 07 -> C1 MensajeAceptacionAnulacion
